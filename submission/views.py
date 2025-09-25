
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.db import transaction
from configurator.models import Config
from runtime_engine.engine import evaluate
from .models import Submission, Outbox
from clinical.models import Patient, Visit
FORM_NAME="visit_opd"
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def submit_visit_opd(request):
    body=request.data or {}
    patient_ext=body.get("patient_id")
    values=body.get("values", {})
    if not patient_ext: return Response({"error":"patient_id is required"}, status=400)
    idem=request.headers.get("Idempotency-Key")
    if not idem: return Response({"error":"Missing Idempotency-Key header"}, status=400)
    existing=Submission.objects.filter(idempotency_key=idem).first()
    if existing: return Response({"status":"duplicate","submission_id":existing.id})
    cfg=Config.objects.filter(kind="rule", name=f"{FORM_NAME}_rules", status="published").order_by("-version").first()
    rules=cfg.spec if cfg else {"rules":[]}
    result=evaluate(values, rules)
    if result["errors"]:
        Submission.objects.create(idempotency_key=idem, form_name=FORM_NAME, payload=values, status="error", errors=result["errors"])
        return Response({"status":"error", "errors":result["errors"]}, status=400)
    for sf in result["setField"]: values[sf["id"]] = sf["value"]
    with transaction.atomic():
        patient,_=Patient.objects.get_or_create(external_id=patient_ext, defaults={"custom_data":{}})
        visit=Visit.objects.create(patient=patient, visit_type="OPD", custom_data=values)
        Submission.objects.create(idempotency_key=idem, form_name=FORM_NAME, payload=values, status="accepted")
        Outbox.objects.create(topic="FormSubmitted", payload={
            "form": FORM_NAME, "patient_id": patient.external_id, "visit_id": visit.id,
            "hba1c": values.get("hba1c"), "book_educator": values.get("book_educator", False),
        })
    return Response({"status":"ok","patient_id":patient.external_id,"visit_id":visit.id,"values":values,"warnings":result["warnings"]})
