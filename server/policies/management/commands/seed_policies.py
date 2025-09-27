from django.core.management.base import BaseCommand
from policies.models import PolicyRule

class Command(BaseCommand):
    help = 'Seed default RBAC policies'

    def handle(self, *args, **options):
        self.stdout.write('Seeding RBAC policies...')
        
        # Clear existing policies
        PolicyRule.objects.all().delete()
        
        # Field-level permissions
        PolicyRule.objects.create(
            tenant_id='H001',
            version=1,
            resource_type='field',
            action='read',
            selector={'form': 'visit_opd', 'field': 'hba1c'},
            effect='allow',
            condition="'Doctor' in user.roles or 'Nurse' in user.roles",
            status='published'
        )
        
        PolicyRule.objects.create(
            tenant_id='H001',
            version=2,
            resource_type='field',
            action='write',
            selector={'form': 'visit_opd', 'field': 'hba1c'},
            effect='allow',
            condition="'Doctor' in user.roles or 'Nurse' in user.roles",
            status='published'
        )
        
        # Nurses can read but mask hiv_status
        PolicyRule.objects.create(
            tenant_id='H001',
            version=3,
            resource_type='field',
            action='read',
            selector={'form': 'visit_opd', 'field': 'hiv_status'},
            effect='allow',
            condition="'Nurse' in user.roles",
            status='published'
        )
        
        PolicyRule.objects.create(
            tenant_id='H001',
            version=4,
            resource_type='field',
            action='mask',
            selector={'form': 'visit_opd', 'field': 'hiv_status'},
            effect='allow',
            condition="'Nurse' in user.roles",
            status='published'
        )
        
        # Deny Nurses from writing hiv_status
        PolicyRule.objects.create(
            tenant_id='H001',
            version=5,
            resource_type='field',
            action='write',
            selector={'form': 'visit_opd', 'field': 'hiv_status'},
            effect='deny',
            condition="'Nurse' in user.roles",
            status='published'
        )
        
        # Allow Doctors to write hiv_status
        PolicyRule.objects.create(
            tenant_id='H001',
            version=6,
            resource_type='field',
            action='write',
            selector={'form': 'visit_opd', 'field': 'hiv_status'},
            effect='allow',
            condition="'Doctor' in user.roles",
            status='published'
        )
        
        # Basic fields - allow all roles
        basic_fields = ['external_id', 'name', 'age', 'height_cm', 'weight_kg', 'bmi']
        for i, field in enumerate(basic_fields, 7):
            PolicyRule.objects.create(
                tenant_id='H001',
                version=i,
                resource_type='field',
                action='read',
                selector={'form': 'visit_opd', 'field': field},
                effect='allow',
                status='published'
            )
            
            PolicyRule.objects.create(
                tenant_id='H001',
                version=i+10,
                resource_type='field',
                action='write',
                selector={'form': 'visit_opd', 'field': field},
                effect='allow',
                status='published'
            )
        
        # Record-level permissions
        PolicyRule.objects.create(
            tenant_id='H001',
            version=20,
            resource_type='record',
            action='read',
            selector={'type': 'visit'},
            effect='allow',
            condition="user.tenant_id == record.custom_data.get('tenant_id', 'H001')",
            status='published'
        )
        
        # Workflow permissions
        PolicyRule.objects.create(
            tenant_id='H001',
            version=21,
            resource_type='workflow',
            action='publish',
            selector={'workflow': 'visit_opd'},
            effect='allow',
            condition="'ClinicalLead' in user.roles or 'Admin' in user.roles",
            status='published'
        )
        
        # Workflow step permissions
        PolicyRule.objects.create(
            tenant_id='H001',
            version=22,
            resource_type='workflow_step',
            action='execute',
            selector={'workflow': 'visit_opd', 'step': 'diabetes_educator'},
            effect='allow',
            condition="'Doctor' in user.roles or 'Nurse' in user.roles",
            status='published'
        )
        
        PolicyRule.objects.create(
            tenant_id='H001',
            version=23,
            resource_type='workflow_step',
            action='execute',
            selector={'workflow': 'visit_opd', 'step': 'pediatrics_birth_certificate'},
            effect='allow',
            condition="'Admin' in user.roles or 'ClinicalLead' in user.roles",
            status='published'
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully seeded {PolicyRule.objects.count()} policies')
        )
