from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Patient, Visit, Document
from .serializers import PatientSerializer, VisitSerializer, DocumentSerializer
from core.tenant import get_current_tenant, require_tenant
from consent.utils import check_consent_for_request, extract_data_categories_from_request

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def patients_list(request):
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    if request.method == 'GET':
        qs = Patient.objects.filter(tenant_id=tenant_id).order_by('-id')[:100]
        return Response(PatientSerializer(qs, many=True).data)
    
    elif request.method == 'POST':
        # Create a new patient directly without creating a visit
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            # Set tenant_id before saving
            patient = serializer.save(tenant_id=tenant_id)
            return Response(PatientSerializer(patient).data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def visits_list(request):
    from policies.authorization import authorize
    from policies.models import PolicyRule
    
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    qs = Visit.objects.filter(tenant_id=tenant_id).order_by('-id')[:100]
    user_claims = getattr(request, 'user_claims', {})
    
    # DISABLED RBAC FILTERING - Show all visits to all roles
    # Return all visits without any filtering
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

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def update_visit_status(request, visit_id):
    """
    Update visit status from pending_consent to completed after consent is created
    """
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    visit = get_object_or_404(Visit, id=visit_id, tenant_id=tenant_id)
    
    if visit.status != 'pending_consent':
        return Response({
            "error": "Visit is not in pending_consent status",
            "current_status": visit.status
        }, status=400)
    
    # Check if consent now exists for this patient
    patient_id = visit.patient.external_id
    data_categories = ['demographics', 'vitals', 'labs', 'diagnosis', 'medications', 'procedures', 'documents']
    
    consent_result = check_consent_for_request(request, patient_id, 'treatment', data_categories)
    
    if not consent_result['allow']:
        return Response({
            "error": "Consent still required",
            "reason": consent_result['reason']
        }, status=400)
    
    # Update visit status to completed
    visit.status = 'completed'
    visit.save()
    
    return Response({
        "status": "success",
        "message": "Visit status updated to completed",
        "visit_id": visit.id,
        "new_status": visit.status
    })

@api_view(['PATCH'])
@permission_classes([AllowAny])
@authentication_classes([])
def update_visit_data(request, visit_id):
    """
    Update visit custom_data for draft or pending_consent visits
    """
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    visit = get_object_or_404(Visit, id=visit_id, tenant_id=tenant_id)
    
    # Only allow editing draft or pending_consent visits
    if visit.status not in ['draft', 'pending_consent']:
        return Response({
            "error": "Visit cannot be edited",
            "current_status": visit.status,
            "allowed_statuses": ["draft", "pending_consent"]
        }, status=400)
    
    # Update custom_data
    if 'custom_data' in request.data:
        visit.custom_data = request.data['custom_data']
        visit.save()
        
        return Response({
            "status": "success",
            "message": "Visit data updated successfully",
            "visit_id": visit.id,
            "updated_data": visit.custom_data
        })
    else:
        return Response({
            "error": "custom_data field is required"
        }, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def complete_draft_visit(request, visit_id):
    """
    Complete a draft visit after consent verification
    """
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    visit = get_object_or_404(Visit, id=visit_id, tenant_id=tenant_id)
    
    # Only allow completing draft or pending_consent visits
    if visit.status not in ['draft', 'pending_consent']:
        return Response({
            "error": "Visit cannot be completed",
            "current_status": visit.status,
            "allowed_statuses": ["draft", "pending_consent"]
        }, status=400)
    
    # Check if consent now exists for this patient
    patient_id = visit.patient.external_id
    data_categories = ['demographics', 'vitals', 'labs', 'diagnosis', 'medications', 'procedures', 'documents']
    
    consent_result = check_consent_for_request(request, patient_id, 'treatment', data_categories)
    
    if not consent_result['allow']:
        return Response({
            "error": "Consent still required",
            "reason": consent_result['reason'],
            "message": "Please create consent for this patient before completing the visit."
        }, status=400)
    
    # Update visit status to completed
    visit.status = 'completed'
    visit.save()
    
    return Response({
        "status": "success",
        "message": "Visit completed successfully",
        "visit_id": visit.id,
        "new_status": visit.status,
        "consent_verified": True
    })