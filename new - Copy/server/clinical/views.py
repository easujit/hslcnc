from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Patient, Visit
from .serializers import PatientSerializer, VisitSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def patients_list(request):
    qs = Patient.objects.order_by('-id')[:100]
    return Response(PatientSerializer(qs, many=True).data)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def visits_list(request):
    qs = Visit.objects.order_by('-id')[:100]
    return Response(VisitSerializer(qs, many=True).data)