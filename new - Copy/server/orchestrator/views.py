from datetime import timedelta
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Outbox, Notification, Task

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def process_now(request):
    created = 0
    for ob in Outbox.objects.filter(published=False).order_by('id'):
        payload = ob.payload_json or {}
        hba1c = payload.get("hba1c")
        patient_name = payload.get("patient_name", "patient")
        if hba1c is not None and float(hba1c) >= 9:
            Notification.objects.create(
                channel="inapp",
                message=f"Book Diabetes Educator session for {patient_name} (HbA1c={hba1c})",
                status="new"
            )
            Task.objects.create(
                team="care",
                summary=f"Educator session for {patient_name}",
                details=f"HbA1c is {hba1c}. Auto-created task from workflow.",
                due_at= now() + timedelta(days=7),
                status="open"
            )
            created += 1
        ob.published = True
        ob.save()
    return Response({"status":"ok","processed_outbox":created})

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def notifications_list(request):
    qs = Notification.objects.order_by('-id')[:100]
    return Response([{"id":n.id,"channel":n.channel,"message":n.message,"status":n.status,"created_at":n.created_at} for n in qs])

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def tasks_list(request):
    qs = Task.objects.order_by('-id')[:100]
    return Response([{"id":t.id,"team":t.team,"summary":t.summary,"details":t.details,"due_at":t.due_at,"status":t.status,"created_at":t.created_at} for t in qs])