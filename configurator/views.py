
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.db import transaction
from .models import Config
from .seeds import FORM_VISIT_OPD, RULES_VISIT_OPD, WORKFLOW_VISIT_OPD

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def seed(request):
    scope={"hospital":"H001","department":"endocrinology"}
    for obj in [FORM_VISIT_OPD, RULES_VISIT_OPD, WORKFLOW_VISIT_OPD]:
        Config.objects.update_or_create(kind=obj["kind"], name=obj["name"], version=1,
            defaults={"status":"published","spec":obj,"scope":scope})
    return Response({"ok":True})

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def effective_form(request, name):
    cfg=Config.objects.filter(kind="form", name=name, status="published").order_by("-version").first()
    if not cfg: return Response({"error":"form not found"}, status=404)
    return Response({"version":cfg.version,"spec":cfg.spec})

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def effective_rules(request, name):
    cfg=Config.objects.filter(kind="rule", name=f"{name}_rules", status="published").order_by("-version").first()
    if not cfg: return Response({"version":0,"spec":{"kind":"rule","name":f"{name}_rules","rules":[]}})
    return Response({"version":cfg.version,"spec":cfg.spec})

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def effective_workflow(request, name):
    cfg=Config.objects.filter(kind="workflow", name=name, status="published").order_by("-version").first()
    if not cfg: return Response({"version":0,"spec":{"kind":"workflow","name":name,"trigger":{},"do":[]}})
    return Response({"version":cfg.version,"spec":cfg.spec})

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def publish_form(request, name):
    spec=request.data or {}
    if not spec.get("kind"): spec["kind"]="form"
    spec["name"]=name
    with transaction.atomic():
        last=Config.objects.filter(kind="form", name=name).order_by("-version").first()
        ver=(last.version+1) if last else 1
        Config.objects.create(kind="form", name=name, version=ver, status="published", spec=spec, scope=spec.get("scope",{"hospital":"H001"}))
    return Response({"ok":True,"version":ver})

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def publish_rules(request, name):
    spec=request.data or {}
    if not spec.get("kind"): spec["kind"]="rule"
    spec["name"]=f"{name}_rules"
    with transaction.atomic():
        last=Config.objects.filter(kind="rule", name=f"{name}_rules").order_by("-version").first()
        ver=(last.version+1) if last else 1
        Config.objects.create(kind="rule", name=f"{name}_rules", version=ver, status="published", spec=spec, scope=spec.get("scope",{"hospital":"H001"}))
    return Response({"ok":True,"version":ver})

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def publish_workflow(request, name):
    spec=request.data or {}
    if not spec.get("kind"): spec["kind"]="workflow"
    with transaction.atomic():
        last=Config.objects.filter(kind="workflow", name=name).order_by("-version").first()
        ver=(last.version+1) if last else 1
        Config.objects.create(kind="workflow", name=name, version=ver, status="published", spec=spec, scope=spec.get("scope",{"hospital":"H001"}))
    return Response({"ok":True,"version":ver})
