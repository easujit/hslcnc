import json
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Config

DEFAULT_FORM = {
  "name": "visit_opd",
  "fields": [
    {"id":"external_id","label":"Patient ID","type":"text","required":True},
    {"id":"name","label":"Name","type":"text","required":True},
    {"id":"age","label":"Age","type":"number","required":True},
    {"id":"height_cm","label":"Height (cm)","type":"number","required":True},
    {"id":"weight_kg","label":"Weight (kg)","type":"number","required":True},
    {"id":"hba1c","label":"HbA1c","type":"number","required":False},
    {"id":"bmi","label":"BMI","type":"number","required":False,"readonly":True},
    {"id":"diabetes_educator_required","label":"Educator Required?","type":"checkbox","required":False,"readonly":True},
    {"id":"diabetes_educator","label":"Book Diabetes Educator session","type":"note","required":False,"visible":False},
    {"id":"guardian_name","label":"Guardian Name","type":"text","required":False,"visible":False},
    {"id":"guardian_relationship","label":"Relationship to Patient","type":"text","required":False,"visible":False},
    {"id":"birth_certificate_upload","label":"Upload Birth Certificate","type":"file","required":False,"visible":False}
  ]
}

DEFAULT_RULES = {
  "calculations":[
    { "set":"bmi", "expr":"round(weight_kg / ((height_cm/100) ** 2), 1)", "when":"height_cm and weight_kg" }
  ],
  "set_fields":[
    { "id":"diabetes_educator_required", "value":"(hba1c is not None) and (hba1c >= 9)" }
  ],
  "visibility":[
    { "id":"diabetes_educator", "when":"(hba1c is not None) and (hba1c >= 9)" },
    { "id":"guardian_name", "when":"(age is not None) and (age < 18)" },
    { "id":"guardian_relationship", "when":"(age is not None) and (age < 18)" },
    { "id":"birth_certificate_upload", "when":"(age is not None) and (age < 18)" }
  ]
}

DEFAULT_WORKFLOW = {
  "post_save":[
    { "emit":"visit_saved" }
  ]
}

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def seed_config(request):
    # seed default OPD configs as published v1/vN
    name = "visit_opd"
    for kind, spec in [('form', DEFAULT_FORM), ('rule', DEFAULT_RULES), ('workflow', DEFAULT_WORKFLOW)]:
        latest = Config.objects.filter(kind=kind, name=name, scope='global').aggregate(Max('version'))['version__max'] or 0
        cfg = Config.objects.create(
            kind=kind, name=name, version=latest+1, status='published', scope='global', spec_json=spec
        )
    return Response({"status":"ok", "message":"Seeded defaults (published)."})

def _effective(kind, name):
    obj = Config.objects.filter(kind=kind, name=name, scope='global', status='published').order_by('-version').first()
    return obj.spec_json if obj else {}

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def effective_form(request, name):
    return Response(_effective('form', name))

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def effective_rules(request, name):
    return Response(_effective('rule', name))

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def effective_workflow(request, name):
    return Response(_effective('workflow', name))

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def publish_config(request, kind, name):
    spec = request.data if isinstance(request.data, dict) else {}
    latest = Config.objects.filter(kind=kind, name=name, scope='global').aggregate(Max('version'))['version__max'] or 0
    cfg = Config.objects.create(kind=kind, name=name, version=latest+1, status='published', scope='global', spec_json=spec)
    return Response({"status":"ok","version":cfg.version})