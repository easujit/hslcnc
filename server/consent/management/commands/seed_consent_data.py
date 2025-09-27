"""
Management command to seed consent data for testing
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from consent.models import Consent, ConsentRequest, AuditEvent

class Command(BaseCommand):
    help = 'Seed consent data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Seeding consent data...')
        
        # Create test consents for different tenants
        tenants = ['TENANT_A', 'TENANT_B', 'DEV']
        
        for tenant in tenants:
            # Clear existing data for this tenant
            Consent.objects.filter(tenant_id=tenant).delete()
            ConsentRequest.objects.filter(tenant_id=tenant).delete()
            AuditEvent.objects.filter(tenant_id=tenant).delete()
            # Create treatment consent for patient P123 (covers all form data categories)
            treatment_consent = Consent.objects.create(
                tenant_id=tenant,
                consent_id=f"CONSENT_TREATMENT_{tenant}_P123",
                patient_id="P123",
                purpose="treatment",
                data_categories=["demographics", "vitals", "labs", "diagnosis", "procedures", "documents"],
                date_range_start=timezone.now() - timedelta(days=30),
                date_range_end=timezone.now() + timedelta(days=365),
                expiry=timezone.now() + timedelta(days=365),
                status="granted",
                notice_lang="en",
                consent_method="digital",
                consent_version="1.0",
                legal_basis="consent"
            )
            
            # Create research consent for patient P456
            research_consent = Consent.objects.create(
                tenant_id=tenant,
                consent_id=f"CONSENT_RESEARCH_{tenant}_P456",
                patient_id="P456",
                purpose="research",
                data_categories=["demographics", "vitals", "labs", "diagnosis"],
                date_range_start=timezone.now() - timedelta(days=15),
                date_range_end=timezone.now() + timedelta(days=180),
                expiry=timezone.now() + timedelta(days=180),
                status="granted",
                notice_lang="en",
                consent_method="digital",
                consent_version="1.0",
                legal_basis="consent"
            )
            
            # Create expired consent for patient P789
            expired_consent = Consent.objects.create(
                tenant_id=tenant,
                consent_id=f"CONSENT_EXPIRED_{tenant}_P789",
                patient_id="P789",
                purpose="treatment",
                data_categories=["demographics", "vitals"],
                date_range_start=timezone.now() - timedelta(days=60),
                date_range_end=timezone.now() - timedelta(days=30),
                expiry=timezone.now() - timedelta(days=30),
                status="expired",
                notice_lang="en",
                consent_method="digital",
                consent_version="1.0",
                legal_basis="consent"
            )
            
            # Create revoked consent for patient P999
            revoked_consent = Consent.objects.create(
                tenant_id=tenant,
                consent_id=f"CONSENT_REVOKED_{tenant}_P999",
                patient_id="P999",
                purpose="treatment",
                data_categories=["demographics", "vitals", "labs"],
                date_range_start=timezone.now() - timedelta(days=10),
                date_range_end=timezone.now() + timedelta(days=355),
                expiry=timezone.now() + timedelta(days=355),
                status="revoked",
                notice_lang="en",
                consent_method="digital",
                consent_version="1.0",
                legal_basis="consent"
            )
            
            self.stdout.write(f'Created consents for tenant {tenant}')
        
        # Create some consent requests
        for tenant in tenants:
            consent_request = ConsentRequest.objects.create(
                tenant_id=tenant,
                request_id=f"REQ_{tenant}_P100",
                patient_id="P100",
                purpose="treatment",
                data_categories=["demographics", "vitals", "labs"],
                abdm_request_id=f"ABDM_REQ_{tenant}_P100",
                abdm_transaction_id=f"TXN_{tenant}_P100",
                status="pending",
                expires_at=timezone.now() + timedelta(hours=24)
            )
            
            self.stdout.write(f'Created consent request for tenant {tenant}')
        
        # Create some audit events
        for tenant in tenants:
            # Create audit event for successful read
            audit_event = AuditEvent.objects.create(
                tenant_id=tenant,
                request_id=f"REQ_AUDIT_{tenant}_001",
                user_id="user123",
                patient_id="P123",
                action="read",
                resource="clinical/patients/P123",
                fields=["name", "age", "hba1c"],
                purpose="treatment",
                data_categories=["demographics", "labs"],
                consent_id=f"CONSENT_TREATMENT_{tenant}_P123",
                decision="ALLOW",
                ip_address="192.168.1.100",
                user_agent="Mozilla/5.0 (Test Browser)",
                reason="Valid consent found"
            )
            
            # Create audit event for denied access
            audit_event_denied = AuditEvent.objects.create(
                tenant_id=tenant,
                request_id=f"REQ_AUDIT_{tenant}_002",
                user_id="user123",
                patient_id="P999",
                action="read",
                resource="clinical/patients/P999",
                fields=["name", "age"],
                purpose="treatment",
                data_categories=["demographics"],
                consent_id=None,
                decision="DENY",
                ip_address="192.168.1.100",
                user_agent="Mozilla/5.0 (Test Browser)",
                reason="No valid consent found"
            )
            
            self.stdout.write(f'Created audit events for tenant {tenant}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully seeded consent data!')
        )
