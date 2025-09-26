import json
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Config
from core.tenant import get_current_tenant, require_tenant
from core.drf_mixins import TenantAwareAPIViewMixin
from consent.compliance_linter import compliance_linter

DEFAULT_FORM = {
  "name": "visit_opd",
  "purpose": "treatment",
  "fields": [
    {"id":"external_id","label":"Patient ID","type":"text","required":True,"data_category":"demographics"},
    {"id":"name","label":"Name","type":"text","required":True,"data_category":"demographics"},
    {"id":"age","label":"Age","type":"number","required":True,"data_category":"demographics"},
    {"id":"height_cm","label":"Height (cm)","type":"number","required":True,"data_category":"vitals"},
    {"id":"weight_kg","label":"Weight (kg)","type":"number","required":True,"data_category":"vitals"},
    {"id":"hba1c","label":"HbA1c","type":"number","required":False,"data_category":"labs"},
    {"id":"bmi","label":"BMI","type":"number","required":False,"readonly":True,"data_category":"vitals"},
    {"id":"diabetes_educator_required","label":"Educator Required?","type":"checkbox","required":False,"readonly":True,"data_category":"diagnosis"},
    {"id":"diabetes_educator","label":"Book Diabetes Educator session","type":"note","required":False,"visible":False,"data_category":"procedures"},
    {"id":"guardian_name","label":"Guardian Name","type":"text","required":False,"visible":False,"data_category":"demographics"},
    {"id":"guardian_relationship","label":"Relationship to Patient","type":"text","required":False,"visible":False,"data_category":"demographics"},
    {"id":"birth_certificate_upload","label":"Upload Birth Certificate","type":"file","required":False,"visible":False,"data_category":"documents"}
  ]
}

DEFAULT_RULES = {
  "purpose": "treatment",
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
  "purpose": "treatment",
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
    tenant_id = get_current_tenant()
    if not tenant_id:
        return {}
    
    obj = Config.objects.filter(
        tenant_id=tenant_id,
        kind=kind, 
        name=name, 
        scope='global', 
        status='published'
    ).order_by('-version').first()
    return obj.spec_json if obj else {}

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def effective_form(request, name):
    # DISABLED RBAC FILTERING - Show all form fields to all roles
    form_spec = _effective('form', name)
    if not form_spec:
        return Response(form_spec)
    
    # Return all form fields without any filtering
    return Response(form_spec)

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
    from policies.authorization import authorize
    
    # Check publish permissions (only if policies exist for this resource type)
    user_claims = getattr(request, 'user_claims', {})
    if user_claims and user_claims.get('tenant_id'):
        from policies.models import PolicyRule
        has_policies = PolicyRule.objects.filter(
            tenant_id=user_claims['tenant_id'],
            resource_type=kind,
            status='published'
        ).exists()
        
        if has_policies:
            can_publish = authorize(
                user_claims, 
                kind, 
                'publish', 
                {kind: name}
            )
            if not can_publish:
                return Response(
                    {"error": f"Insufficient permissions to publish {kind}"}, 
                    status=403
                )
    
    # Ensure tenant context exists
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    spec = request.data if isinstance(request.data, dict) else {}
    
    # Compliance linting
    if kind == 'form':
        is_valid, errors, warnings = compliance_linter.lint_form(spec)
    elif kind == 'rule':
        is_valid, errors, warnings = compliance_linter.lint_rules(spec)
    elif kind == 'workflow':
        is_valid, errors, warnings = compliance_linter.lint_workflow(spec)
    else:
        is_valid, errors, warnings = True, [], []
    
    if not is_valid:
        return Response({
            "error": "Compliance validation failed",
            "details": errors,
            "warnings": warnings
        }, status=400)
    
    if warnings:
        # Log warnings but allow publishing
        print(f"Compliance warnings for {kind}/{name}: {warnings}")
    
    latest = Config.objects.filter(
        tenant_id=tenant_id,
        kind=kind, 
        name=name, 
        scope='global'
    ).aggregate(Max('version'))['version__max'] or 0
    
    cfg = Config.objects.create(
        tenant_id=tenant_id,
        kind=kind, 
        name=name, 
        version=latest+1, 
        status='published', 
        scope='global', 
        spec_json=spec
    )
    return Response({"status":"ok","version":cfg.version, "warnings": warnings})

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_versions(request, kind, name):
    """Get version history for a specific configuration type"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    versions = Config.objects.filter(
        tenant_id=tenant_id,
        kind=kind,
        name=name,
        scope='global'
    ).order_by('-version').values(
        'version', 'status', 'created_at', 'updated_at'
    )
    
    return Response(list(versions))

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def rollback_config(request, kind, name):
    """Rollback to a specific version of a configuration"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    target_version = request.data.get('version')
    if not target_version:
        return Response({"error": "Version number required"}, status=400)
    
    # Find the target version
    target_config = Config.objects.filter(
        tenant_id=tenant_id,
        kind=kind,
        name=name,
        version=target_version,
        scope='global'
    ).first()
    
    if not target_config:
        return Response({"error": f"Version {target_version} not found"}, status=404)
    
    # Get the latest version
    latest = Config.objects.filter(
        tenant_id=tenant_id,
        kind=kind,
        name=name,
        scope='global'
    ).aggregate(Max('version'))['version__max'] or 0
    
    # Create a new version with the target config's spec
    new_config = Config.objects.create(
        tenant_id=tenant_id,
        kind=kind,
        name=name,
        version=latest+1,
        status='published',
        scope='global',
        spec_json=target_config.spec_json
    )
    
    return Response({
        "status": "ok",
        "message": f"Rolled back to version {target_version}",
        "new_version": new_config.version
    })