
import math
def safe_eval_expr(expr, ctx):
    allowed={"round":round,"math":math}
    return eval(expr, {"__builtins__": {}}, {**allowed, **ctx})
def evaluate(values: dict, rules_spec: dict):
    errors, warnings, set_field, visibility = [], [], [], []
    ctx = dict(values)
    for rule in rules_spec.get("rules", []):
        cond = rule.get("when") or "False"
        try: cond_ok = eval(cond, {"__builtins__": {}}, ctx)
        except Exception: cond_ok = False
        if not cond_ok: continue
        for action in rule.get("then", []):
            if "set_field" in action:
                a=action["set_field"]
                try: val = safe_eval_expr(a["expr"], ctx)
                except Exception: val = None
                set_field.append({"id":a["id"], "value":val})
                ctx[a["id"]] = val
            elif "set_visibility" in action:
                a=action["set_visibility"]
                visibility.append({"id":a["id"], "visible": a.get("visible", True)})
            elif "banner" in action:
                warnings.append(action["banner"].get("text",""))
    return {"errors":errors,"warnings":warnings,"setField":set_field,"visibility":visibility}
