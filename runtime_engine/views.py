
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from configurator.models import Config
from .engine import evaluate
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def evaluate_rules(request, form_name):
    cfg = Config.objects.filter(kind="rule", name=f"{form_name}_rules", status="published").order_by("-version").first()
    rules = cfg.spec if cfg else {"rules":[]}
    values = request.data.get("values", {})
    result = evaluate(values, rules)
    return Response(result)
