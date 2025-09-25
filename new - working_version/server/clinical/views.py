from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Patient, Visit, Document
from .serializers import PatientSerializer, VisitSerializer, DocumentSerializer

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

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def upload_document(request):
    if 'file' not in request.FILES:
        return Response({"error": "No file provided"}, status=400)
    
    patient_id = request.data.get('patient_id')
    visit_id = request.data.get('visit_id')
    document_type = request.data.get('document_type', 'birth_certificate')
    
    if not patient_id:
        return Response({"error": "Patient ID required"}, status=400)
    
    try:
        patient = Patient.objects.get(id=patient_id)
        visit = Visit.objects.get(id=visit_id) if visit_id else None
        
        document = Document.objects.create(
            patient=patient,
            visit=visit,
            document_type=document_type,
            file=request.FILES['file']
        )
        
        return Response({
            "status": "success",
            "document_id": document.id,
            "file_url": document.file.url,
            "file_size": document.file_size
        })
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=404)
    except Visit.DoesNotExist:
        return Response({"error": "Visit not found"}, status=404)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def patient_documents(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
        documents = Document.objects.filter(patient=patient).order_by('-uploaded_at')
        return Response(DocumentSerializer(documents, many=True).data)
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=404)