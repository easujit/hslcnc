import ast
import operator as op
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from configurator.models import Config
from consent.utils import check_consent_for_request, extract_data_categories_from_request

# Allowed operators and names for safe evaluation
_ALLOWED_BINOP = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv,
    ast.Pow: op.pow, ast.Mod: op.mod, ast.FloorDiv: op.floordiv
}
_ALLOWED_CMPOP = {
    ast.Eq: op.eq, ast.NotEq: op.ne, ast.Lt: op.lt, ast.LtE: op.le, ast.Gt: op.gt, ast.GtE: op.ge,
    ast.Is: lambda x, y: x is y, ast.IsNot: lambda x, y: x is not y
}
_ALLOWED_BOOL = {ast.And: all, ast.Or: any}

def _safe_eval(expr, variables):
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            return variables.get(node.id)
        if isinstance(node, ast.BinOp):
            if type(node.op) not in _ALLOWED_BINOP:
                raise ValueError("Operator not allowed")
            return _ALLOWED_BINOP[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                return -_eval(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +_eval(node.operand)
        if isinstance(node, ast.BoolOp):
            if type(node.op) not in _ALLOWED_BOOL:
                raise ValueError("Bool op not allowed")
            vals = [_eval(v) for v in node.values]
            return _ALLOWED_BOOL[type(node.op)]([bool(v) for v in vals])
        if isinstance(node, ast.Compare):
            left = _eval(node.left)
            result = True
            for opnode, comparator in zip(node.ops, node.comparators):
                right = _eval(comparator)
                if type(opnode) not in _ALLOWED_CMPOP:
                    raise ValueError("Comparison not allowed")
                if not _ALLOWED_CMPOP[type(opnode)](left, right):
                    result = False
                    break
                left = right
            return result
        if isinstance(node, ast.Call):
            # allow round(x, n) only
            if not isinstance(node.func, ast.Name) or node.func.id not in ['round']:
                raise ValueError("Function not allowed")
            args = [_eval(a) for a in node.args]
            return round(*args)
        if isinstance(node, ast.IfExp):
            return _eval(node.body) if _eval(node.test) else _eval(node.orelse)
        if isinstance(node, ast.Attribute):
            raise ValueError("Attribute access not allowed")
        raise ValueError("Unsupported expression")

    tree = ast.parse(expr, mode='eval')
    return _eval(tree)

def evaluate_spec(spec, data):
    errors, warnings = [], []
    setField, visibility = [], []

    # calculations
    for c in spec.get("calculations", []):
        try:
            cond = c.get("when")
            ok = True
            if cond:
                ok = bool(_safe_eval(str(cond), data))
            if ok:
                val = _safe_eval(str(c.get("expr")), data)
                setField.append({"id": c.get("set"), "value": val})
        except Exception as e:
            warnings.append(f"calc error for {c}: {e}")

    # set_fields
    for s in spec.get("set_fields", []):
        try:
            val_expr = s.get("value")
            val = bool(_safe_eval(str(val_expr), data)) if isinstance(val_expr, str) else val_expr
            setField.append({"id": s.get("id"), "value": val})
        except Exception as e:
            warnings.append(f"set_fields error for {s}: {e}")

    # visibility
    for v in spec.get("visibility", []):
        try:
            cond = v.get("when")
            vis = bool(_safe_eval(str(cond), data)) if cond is not None else True
            visibility.append({"id": v.get("id"), "visible": vis})
        except Exception as e:
            warnings.append(f"visibility error for {v}: {e}")

    # Extension functions - runtime.compute and runtime.validate
    try:
        from extensions.models import ExtensionFunction
        from extensions.utils import call_http, create_webhook_headers, matches_criteria
        
        # Get matching extension functions
        extension_functions = ExtensionFunction.objects.filter(
            enabled=True,
            type__in=['runtime.compute', 'runtime.validate']
        )
        
        for ext_func in extension_functions:
            # Check if this function matches the current context
            if not matches_criteria(data, ext_func.match_json):
                continue
                
            invoke_config = ext_func.invoke_json
            url = invoke_config.get('url')
            method = invoke_config.get('method', 'POST')
            timeout_ms = min(invoke_config.get('timeout_ms', 5000), 1200)  # Max 1200ms for runtime
            headers = invoke_config.get('headers', {})
            
            if not url:
                warnings.append(f"Extension function {ext_func.name} has no URL")
                continue
            
            # Prepare payload
            payload = {
                'form_data': data,
                'function_type': ext_func.type,
                'function_name': ext_func.name
            }
            
            # Add HMAC signature
            webhook_headers = create_webhook_headers(payload, ext_func.secret)
            webhook_headers.update(headers)
            
            # Call extension function
            success, status_code, response_data, error_msg = call_http(
                url=url,
                method=method,
                json_data=payload,
                timeout_ms=timeout_ms,
                headers=webhook_headers,
                retries=1  # Only 1 retry for runtime functions
            )
            
            if success and status_code == 200:
                # Merge response data
                ext_setField = response_data.get('setField', [])
                ext_visibility = response_data.get('visibility', [])
                ext_warnings = response_data.get('warnings', [])
                ext_errors = response_data.get('errors', [])
                
                setField.extend(ext_setField)
                visibility.extend(ext_visibility)
                warnings.extend([f"[{ext_func.name}] {w}" for w in ext_warnings])
                errors.extend([f"[{ext_func.name}] {e}" for e in ext_errors])
                
            else:
                error_msg = error_msg or f"HTTP {status_code}: {response_data}"
                if ext_func.is_blocking:
                    warnings.append(f"Extension function {ext_func.name} failed (blocking): {error_msg}")
                else:
                    warnings.append(f"Extension function {ext_func.name} failed (non-blocking): {error_msg}")
                    
    except Exception as e:
        warnings.append(f"Extension function error: {str(e)}")

    return { "errors": errors, "warnings": warnings, "setField": setField, "visibility": visibility }

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def evaluate_rules(request, form):
    from core.tenant import get_current_tenant
    
    # Get effective rules for form
    tenant_id = get_current_tenant()
    obj = Config.objects.filter(
        tenant_id=tenant_id,
        kind='rule', 
        name=form, 
        status='published'
    ).order_by('-version').first()
    spec = obj.spec_json if obj else {}
    data = request.data if isinstance(request.data, dict) else {}
    
    # Consent enforcement - check if patient has consent for form access
    patient_id = data.get('external_id') or data.get('patient_id')
    if patient_id:
        # Extract data categories from form configuration
        form_obj = Config.objects.filter(
            tenant_id=tenant_id,
            kind='form', 
            name=form, 
            status='published'
        ).order_by('-version').first()
        
        if form_obj and 'fields' in form_obj.spec_json:
            data_categories = []
            for field in form_obj.spec_json['fields']:
                if 'data_category' in field:
                    data_categories.append(field['data_category'])
        else:
            data_categories = extract_data_categories_from_request(request)
        
        purpose = spec.get('purpose', 'treatment')
        
        # Check consent
        consent_result = check_consent_for_request(request, patient_id, purpose, data_categories)
        
        if not consent_result['allow']:
            return Response({
                "errors": [f"Consent required: {consent_result['reason']}"],
                "warnings": [],
                "setField": [],
                "visibility": []
            }, status=403)
    
    result = evaluate_spec(spec, data)
    
    # Apply consent-based field filtering
    if patient_id and 'fields' in (form_obj.spec_json if form_obj else {}):
        filtered_visibility = []
        for field in form_obj.spec_json['fields']:
            field_id = field['id']
            field_category = field.get('data_category', 'demographics')
            
            # Check if patient has consent for this data category
            if field_category in data_categories:
                # Find existing visibility rule for this field
                existing_rule = next((v for v in result['visibility'] if v['id'] == field_id), None)
                if existing_rule:
                    filtered_visibility.append(existing_rule)
                else:
                    filtered_visibility.append({"id": field_id, "visible": True})
            else:
                # Hide field if no consent for this category
                filtered_visibility.append({"id": field_id, "visible": False})
        
        result['visibility'] = filtered_visibility
    
    return Response(result)