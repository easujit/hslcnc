import ast
import operator as op
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from configurator.models import Config

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

    return { "errors": errors, "warnings": warnings, "setField": setField, "visibility": visibility }

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def evaluate_rules(request, form):
    # Get effective rules for form
    obj = Config.objects.filter(kind='rule', name=form, status='published').order_by('-version').first()
    spec = obj.spec_json if obj else {{}}
    data = request.data if isinstance(request.data, dict) else {{}}
    result = evaluate_spec(spec, data)
    return Response(result)