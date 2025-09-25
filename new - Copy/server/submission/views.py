from datetime import datetime
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from configurator.models import Config
from runtime_engine.views import evaluate_spec
from clinical.models import Patient, Visit
from .models import Submission
from orchestrator.models import Outbox

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

    # enqueue outbox event
    Outbox.objects.create(topic="visit_saved", payload_json={
        "visit_id": visit.id, "patient_external_id": patient.external_id, "patient_name": patient.name,
        "hba1c": payload.get("hba1c"), "bmi": payload.get("bmi")
    })

    sub.status = 'processed'
    sub.payload_json["_result"] = {"visit_id": visit.id, "patient_id": patient.id, "bmi": payload.get("bmi"),
                                   "diabetes_educator_required": payload.get("diabetes_educator_required", False)}
    sub.save()
    return Response({"status":"ok","idempotent":False, **sub.payload_json["_result"]})