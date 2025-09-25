#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetes_poc.settings')
django.setup()

from configurator.models import Config
from runtime_engine.views import evaluate_spec

# Check current form configuration
print("=== CURRENT FORM CONFIG ===")
form_config = Config.objects.filter(kind='form', name='visit_opd', status='published').order_by('-version').first()
if form_config:
    print(f"Form version: {form_config.version}")
    print("Fields:")
    for field in form_config.spec_json.get('fields', []):
        print(f"  - {field['id']}: {field['label']} ({field['type']}) - visible: {field.get('visible', True)}")
else:
    print("No form config found!")

print("\n=== CURRENT RULES CONFIG ===")
rules_config = Config.objects.filter(kind='rule', name='visit_opd', status='published').order_by('-version').first()
if rules_config:
    print(f"Rules version: {rules_config.version}")
    print("Visibility rules:")
    for rule in rules_config.spec_json.get('visibility', []):
        print(f"  - {rule['id']}: {rule['when']}")
else:
    print("No rules config found!")

print("\n=== TESTING RULES EVALUATION ===")
# Test with age 12
test_data = {"age": 12, "name": "John", "height_cm": 150, "weight_kg": 45}
print(f"Test data: {test_data}")

if rules_config:
    result = evaluate_spec(rules_config.spec_json, test_data)
    print(f"Evaluation result: {result}")
else:
    print("Cannot test - no rules config!")

print("\n=== TESTING RULES EVALUATION WITH AGE 20 ===")
# Test with age 20
test_data_adult = {"age": 20, "name": "Jane", "height_cm": 170, "weight_kg": 65}
print(f"Test data: {test_data_adult}")

if rules_config:
    result_adult = evaluate_spec(rules_config.spec_json, test_data_adult)
    print(f"Evaluation result: {result_adult}")
else:
    print("Cannot test - no rules config!")
