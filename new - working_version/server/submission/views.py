from datetime import datetime, timedelta
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from configurator.models import Config
from runtime_engine.views import evaluate_spec
from clinical.models import Patient, Visit, Document
from .models import Submission
from orchestrator.models import Outbox, Task

def _get_effective_rules(form_name):
    obj = Config.objects.filter(kind='rule', name=form_name, status='published').order_by('-version').first()
    return obj.spec_json if obj else {}

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def submit_visit_opd(request):
    idem = request.headers.get('Idempotency-Key') or request.META.get('HTTP_IDEMPOTENCY_KEY')
    if not idem:
        return Response({"error":"Missing Idempotency-Key header"}, status=400)

    existing = Submission.objects.filter(idempotency_key=idem).first()
    if existing and existing.status == 'processed':
        # Return idempotent response
        result = existing.payload_json.get("_result", {})
        return Response({"status":"ok","idempotent":True, **result})

    payload = request.data if isinstance(request.data, dict) else {}
    rules = _get_effective_rules("visit_opd")
    eval_out = evaluate_spec(rules, payload)

    # apply setField
    for sf in eval_out.get("setField", []):
        payload[sf["id"]] = sf["value"]

    sub = existing or Submission.objects.create(idempotency_key=idem, form_name="visit_opd", payload_json=payload)

    # Get effective form configuration for validation
    form_config = Config.objects.filter(kind='form', name='visit_opd', status='published').order_by('-version').first()
    if not form_config:
        sub.status = 'error'
        sub.errors_json = ["Form configuration not found"]
        sub.save()
        return Response({"error":"Form configuration not found"}, status=500)

    # Validate required fields
    validation_errors = []
    for field in form_config.spec_json.get('fields', []):
        if field.get('required', False):
            field_id = field['id']
            field_value = payload.get(field_id)
            if field_value is None or field_value == '' or field_value == 0:
                validation_errors.append(f"{field['label']} is required")
    
    if validation_errors:
        sub.status = 'error'
        sub.errors_json = validation_errors
        sub.save()
        return Response({"error": validation_errors[0], "errors": validation_errors}, status=400)

    # Upsert patient
    ext = payload.get("external_id")
    name = payload.get("name", "Unknown")
    if not ext:
        sub.status = 'error'
        sub.errors_json = ["external_id required"]
        sub.save()
        return Response({"error":"external_id required"}, status=400)
    patient, _ = Patient.objects.get_or_create(external_id=ext, defaults={"name": name})
    if patient.name != name and name:
        patient.name = name
        patient.save()

    visit = Visit.objects.create(patient=patient, visit_type="OPD", custom_data=payload)

    # Check for pediatrics guardian requirements
    age = payload.get("age")
    is_minor = age is not None and int(age) < 18
    guardian_name = payload.get("guardian_name")
    has_birth_certificate = Document.objects.filter(patient=patient, document_type="birth_certificate").exists()
    
    # Validation: Cannot save if age < 18 and no guardian
    if is_minor and not guardian_name:
        sub.status = 'error'
        sub.errors_json = ["Guardian name is required for patients under 18"]
        sub.save()
        return Response({"error": "Guardian name is required for patients under 18"}, status=400)

    # enqueue outbox event
    outbox_payload = {
        "visit_id": visit.id, 
        "patient_external_id": patient.external_id, 
        "patient_name": patient.name,
        "hba1c": payload.get("hba1c"), 
        "bmi": payload.get("bmi"),
        "age": age,
        "is_minor": is_minor,
        "guardian_name": guardian_name,
        "has_birth_certificate": has_birth_certificate
    }
    
    Outbox.objects.create(topic="visit_saved", payload_json=outbox_payload)

    sub.status = 'processed'
    sub.payload_json["_result"] = {
        "visit_id": visit.id, 
        "patient_id": patient.id, 
        "bmi": payload.get("bmi"),
        "diabetes_educator_required": payload.get("diabetes_educator_required", False),
        "is_minor": is_minor,
        "guardian_required": is_minor and not guardian_name,
        "birth_certificate_required": is_minor and not has_birth_certificate
    }
    sub.save()
    return Response({"status":"ok","idempotent":False, **sub.payload_json["_result"]})