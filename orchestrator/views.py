
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from submission.models import Outbox
from configurator.models import Config
from .models import Notification, Task

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def list_notifications(request):
    qs = Notification.objects.order_by('-created_at')[:100]
    data = [{
        "id": n.id, "channel": n.channel, "message": n.message,
        "status": n.status, "created_at": n.created_at.isoformat()
    } for n in qs]
    return Response(data)

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def list_tasks(request):
    qs = Task.objects.order_by('-created_at')[:100]
    data = [{
        "id": t.id, "team": t.team, "summary": t.summary, "details": t.details,
        "due_at": t.due_at.isoformat(), "status": t.status, "created_at": t.created_at.isoformat()
    } for t in qs]
    return Response(data)

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def process_now(request):
    events = Outbox.objects.filter(published=False).order_by("created_at")[:100]
    processed = 0
    for ev in events:
        if ev.topic == "FormSubmitted" and ev.payload.get("form") == "visit_opd":
            wf = Config.objects.filter(kind="workflow", name="high_hba1c_followup", status="published").order_by("-version").first()
            h = ev.payload.get("hba1c")
            try:
                hv = float(h) if h is not None else None
            except Exception:
                hv = None
            if hv is not None and hv >= 9:
                Notification.objects.create(
                    channel="endocrinology_on_call",
                    message=f"High HbA1c ({hv}%) for patient {ev.payload.get('patient_id')}",
                    status="sent"
                )
                Task.objects.create(
                    team="diabetes_education",
                    summary="Schedule educator session",
                    details=f"HbA1c={hv}, visit_id={ev.payload.get('visit_id')}",
                    due_at=timezone.now() + timedelta(days=7),
                    status="open"
                )
        ev.published = True
        ev.save(update_fields=["published"])
        processed += 1
    return Response({"processed": processed})
