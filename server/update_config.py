#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetes_poc.settings')
django.setup()

from configurator.models import Config

# Update the form configuration with pediatrics fields
form_config = {
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

rules_config = {
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

workflow_config = {
  "post_save":[
    { "emit":"visit_saved" }
  ]
}

# Get the latest version numbers
latest_form = Config.objects.filter(kind='form', name='visit_opd', scope='global').order_by('-version').first()
latest_rules = Config.objects.filter(kind='rule', name='visit_opd', scope='global').order_by('-version').first()
latest_workflow = Config.objects.filter(kind='workflow', name='visit_opd', scope='global').order_by('-version').first()

# Create new versions
form_version = (latest_form.version + 1) if latest_form else 1
rules_version = (latest_rules.version + 1) if latest_rules else 1
workflow_version = (latest_workflow.version + 1) if latest_workflow else 1

# Create new configurations
Config.objects.create(
    kind='form', 
    name='visit_opd', 
    version=form_version, 
    status='published', 
    scope='global', 
    spec_json=form_config
)

Config.objects.create(
    kind='rule', 
    name='visit_opd', 
    version=rules_version, 
    status='published', 
    scope='global', 
    spec_json=rules_config
)

Config.objects.create(
    kind='workflow', 
    name='visit_opd', 
    version=workflow_version, 
    status='published', 
    scope='global', 
    spec_json=workflow_config
)

print(f"Updated form to version {form_version}")
print(f"Updated rules to version {rules_version}")
print(f"Updated workflow to version {workflow_version}")
print("Pediatrics fields should now appear when age < 18")
