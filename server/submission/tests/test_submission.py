from django.test import TestCase
from rest_framework.test import APIClient
from configurator.models import Config

class SubmissionIdempotencyTest(TestCase):
    def setUp(self):
        form = {"name":"visit_opd","fields":[{"id":"external_id"},{"id":"name"},{"id":"height_cm"},{"id":"weight_kg"},{"id":"hba1c"},{"id":"bmi"},{"id":"diabetes_educator_required"}]}
        rules = {
            "calculations":[
                { "set":"bmi", "expr":"round(weight_kg / ((height_cm/100) ** 2), 1)", "when":"height_cm and weight_kg" }
            ],
            "set_fields":[
                { "id":"diabetes_educator_required", "value":"(hba1c is not None) and (hba1c >= 9)" }
            ]
        }
        Config.objects.create(kind='form', name='visit_opd', version=1, status='published', scope='global', spec_json=form)
        Config.objects.create(kind='rule', name='visit_opd', version=1, status='published', scope='global', spec_json=rules)

    def test_idempotent_submission(self):
        client = APIClient()
        payload = {"external_id":"P001","name":"Alice","height_cm":170,"weight_kg":68,"hba1c":8.0}
        headers = {"HTTP_IDEMPOTENCY_KEY":"abc123"}
        r1 = client.post("/api/submit/forms/visit_opd/submit/", payload, format="json", **headers)
        self.assertEqual(r1.status_code, 200)
        visit_id_1 = r1.json()["visit_id"]
        bmi_1 = r1.json()["bmi"]
        self.assertAlmostEqual(bmi_1, 23.5)

        r2 = client.post("/api/submit/forms/visit_opd/submit/", payload, format="json", **headers)
        self.assertEqual(r2.status_code, 200)
        self.assertTrue(r2.json().get("idempotent"))
        self.assertEqual(r2.json()["visit_id"], visit_id_1)