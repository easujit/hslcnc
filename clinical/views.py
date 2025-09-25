
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Patient, Visit

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def list_visits(request):
    qs = Visit.objects.select_related('patient').order_by('-created_at')[:100]
    data = [{
        "id": v.id,
        "patient": v.patient.external_id,
        "custom_data": v.custom_data,
        "created_at": v.created_at.isoformat()
    } for v in qs]
    return Response(data)

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def list_patients(request):
    qs = Patient.objects.order_by('-created_at')[:100]
    data = [{
        "id": p.id,
        "external_id": p.external_id,
        "custom_data": p.custom_data,
        "created_at": p.created_at.isoformat()
    } for p in qs]
    return Response(data)
