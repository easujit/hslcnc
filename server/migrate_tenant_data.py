#!/usr/bin/env python
"""
Data migration script to add tenant_id to existing records
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetes_poc.settings')
django.setup()

from django.db import transaction
from configurator.models import Config
from clinical.models import Patient, Visit, Document
from submission.models import Submission
from orchestrator.models import Outbox, Notification, Task
from policies.models import PolicyRule

def migrate_tenant_data():
    """Add tenant_id to existing records"""
    print("=== Starting Tenant Data Migration ===")
    
    # Default tenant for existing data
    default_tenant = "DEV"
    
    with transaction.atomic():
        # Migrate Config records
        config_count = Config.objects.filter(tenant_id__isnull=True).count()
        if config_count > 0:
            Config.objects.filter(tenant_id__isnull=True).update(tenant_id=default_tenant)
            print(f"Updated {config_count} Config records with tenant_id={default_tenant}")
        
        # Migrate Patient records
        patient_count = Patient.objects.filter(tenant_id__isnull=True).count()
        if patient_count > 0:
            Patient.objects.filter(tenant_id__isnull=True).update(tenant_id=default_tenant)
            print(f"Updated {patient_count} Patient records with tenant_id={default_tenant}")
        
        # Migrate Visit records
        visit_count = Visit.objects.filter(tenant_id__isnull=True).count()
        if visit_count > 0:
            Visit.objects.filter(tenant_id__isnull=True).update(tenant_id=default_tenant)
            print(f"Updated {visit_count} Visit records with tenant_id={default_tenant}")
        
        # Migrate Document records
        document_count = Document.objects.filter(tenant_id__isnull=True).count()
        if document_count > 0:
            Document.objects.filter(tenant_id__isnull=True).update(tenant_id=default_tenant)
            print(f"Updated {document_count} Document records with tenant_id={default_tenant}")
        
        # Migrate Submission records
        submission_count = Submission.objects.filter(tenant_id__isnull=True).count()
        if submission_count > 0:
            Submission.objects.filter(tenant_id__isnull=True).update(tenant_id=default_tenant)
            print(f"Updated {submission_count} Submission records with tenant_id={default_tenant}")
        
        # Migrate Outbox records
        outbox_count = Outbox.objects.filter(tenant_id__isnull=True).count()
        if outbox_count > 0:
            Outbox.objects.filter(tenant_id__isnull=True).update(tenant_id=default_tenant)
            print(f"Updated {outbox_count} Outbox records with tenant_id={default_tenant}")
        
        # Migrate Notification records
        notification_count = Notification.objects.filter(tenant_id__isnull=True).count()
        if notification_count > 0:
            Notification.objects.filter(tenant_id__isnull=True).update(tenant_id=default_tenant)
            print(f"Updated {notification_count} Notification records with tenant_id={default_tenant}")
        
        # Migrate Task records
        task_count = Task.objects.filter(tenant_id__isnull=True).count()
        if task_count > 0:
            Task.objects.filter(tenant_id__isnull=True).update(tenant_id=default_tenant)
            print(f"Updated {task_count} Task records with tenant_id={default_tenant}")
        
        # Migrate PolicyRule records
        policy_count = PolicyRule.objects.filter(tenant_id__isnull=True).count()
        if policy_count > 0:
            PolicyRule.objects.filter(tenant_id__isnull=True).update(tenant_id=default_tenant)
            print(f"Updated {policy_count} PolicyRule records with tenant_id={default_tenant}")
    
    print("=== Tenant Data Migration Complete ===")

if __name__ == '__main__':
    migrate_tenant_data()
