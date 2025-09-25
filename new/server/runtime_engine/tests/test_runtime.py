from django.test import TestCase
from configurator.models import Config
from runtime_engine.views import evaluate_spec

class RuntimeRulesTest(TestCase):
    def setUp(self):
        rules = {
            "calculations":[
                { "set":"bmi", "expr":"round(weight_kg / ((height_cm/100) ** 2), 1)", "when":"height_cm and weight_kg" }
            ],
            "set_fields":[
                { "id":"diabetes_educator_required", "value":"(hba1c is not None) and (hba1c >= 9)" }
            ],
            "visibility":[
                { "id":"diabetes_educator", "when":"(hba1c is not None) and (hba1c >= 9)" }
            ]
        }
        Config.objects.create(kind='rule', name='visit_opd', version=1, status='published', scope='global', spec_json=rules)

    def test_bmi_calc_and_hba1c_flag(self):
        data = {"height_cm":170, "weight_kg":68, "hba1c":9.1}
        rules = Config.objects.get(kind='rule', name='visit_opd', version=1).spec_json
        out = evaluate_spec(rules, data)
        sf = {s["id"]: s["value"] for s in out["setField"]}
        vis = {v["id"]: v["visible"] for v in out["visibility"]}
        self.assertAlmostEqual(sf["bmi"], 23.5)
        self.assertTrue(sf["diabetes_educator_required"])
        self.assertTrue(vis["diabetes_educator"])