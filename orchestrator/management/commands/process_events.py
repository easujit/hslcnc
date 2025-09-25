
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from submission.models import Outbox
from configurator.models import Config
from orchestrator.models import Notification, Task
class Command(BaseCommand):
    help="Process outbox events and run workflows"
    def handle(self, *args, **kwargs):
        events=Outbox.objects.filter(published=False).order_by("created_at")[:100]
        if not events:
            self.stdout.write("No events."); return
        n=0
        for ev in events:
            if ev.topic=="FormSubmitted" and ev.payload.get("form")=="visit_opd":
                wf=Config.objects.filter(kind="workflow", name="high_hba1c_followup", status="published").order_by("-version").first()
                h=ev.payload.get("hba1c")
                try: hv=float(h) if h is not None else None
                except: hv=None
                if hv is not None and hv>=9:
                    Notification.objects.create(channel="endocrinology_on_call", message=f"High HbA1c ({hv}%) for patient {ev.payload.get('patient_id')}", status="sent")
                    Task.objects.create(team="diabetes_education", summary="Schedule educator session", details=f"HbA1c={hv}, visit_id={ev.payload.get('visit_id')}", due_at=timezone.now()+timedelta(days=7), status="open")
            ev.published=True; ev.save(update_fields=["published"]); n+=1
        self.stdout.write(f"Processed {n} event(s).")
