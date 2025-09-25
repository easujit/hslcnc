# Consent Management System (DPDP + ABDM Compliance)

## Overview

This document describes the comprehensive Consent Management system implemented for DPDP (Digital Personal Data Protection) and ABDM (Ayushman Bharat Digital Mission) compliance. The system ensures that every data access, write, and share operation is consent-gated and audited.

## Architecture

### Core Components

1. **Consent Models** (`consent/models.py`)
   - `Consent`: Patient consent records with purpose, data categories, and validity
   - `ConsentRequest`: ABDM consent request state management
   - `AuditEvent`: Immutable audit log with hash chain integrity

2. **Compliance Linter** (`consent/compliance_linter.py`)
   - Validates form, rules, and workflow specifications for compliance
   - Ensures all fields have data categories and all specs have purposes

3. **Audit Middleware** (`consent/audit_middleware.py`)
   - WORM-like logging of all data access operations
   - Hash chain integrity for tamper-proof audit trail

4. **ABDM Connector** (`consent/abdm_connector.py`)
   - Handles ABDM consent request lifecycle
   - Manages consent artefacts and notifications

## Data Model

### Consent Model

```python
class Consent(AbstractTenantModel):
    consent_id = models.CharField(max_length=100, unique=True)
    patient_id = models.CharField(max_length=100)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)
    data_categories = models.JSONField(default=list)
    date_range_start = models.DateTimeField()
    date_range_end = models.DateTimeField()
    expiry = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notice_lang = models.CharField(max_length=10, default='en')
    withdraw_url = models.URLField(blank=True, null=True)
    abdm_artefact_id = models.CharField(max_length=200, blank=True, null=True)
```

### AuditEvent Model

```python
class AuditEvent(AbstractTenantModel):
    timestamp = models.DateTimeField(auto_now_add=True)
    request_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=100)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    resource = models.CharField(max_length=200)
    fields = models.JSONField(default=list)
    purpose = models.CharField(max_length=50)
    data_categories = models.JSONField(default=list)
    consent_id = models.CharField(max_length=100, blank=True, null=True)
    decision = models.CharField(max_length=10, choices=DECISION_CHOICES)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    event_hash = models.CharField(max_length=64, unique=True)
    previous_hash = models.CharField(max_length=64, blank=True, null=True)
```

## API Endpoints

### Consent Management

- `POST /api/consent/consents/` - Create new consent
- `GET /api/consent/consents/{consent_id}/` - Get consent details
- `POST /api/consent/consent/{consent_id}/revoke/` - Revoke consent
- `GET /api/consent/patients/{patient_id}/consents/` - Get patient consents

### Consent Checking

- `POST /api/consent/consent/check/` - Check consent for operation
  ```json
  {
    "patient_id": "P123",
    "purpose": "treatment",
    "data_categories": ["demographics", "vitals"],
    "action": "read"
  }
  ```

### ABDM Integration

- `POST /api/consent/abdm/request-consent/` - Create ABDM consent request
- `POST /api/consent/abdm/notify/` - Handle ABDM notification
- `POST /api/consent/abdm/fetch-artefact/` - Fetch consent artefact

### Audit Events

- `GET /api/consent/audit-events/` - List audit events
- `GET /api/consent/audit-events/?patient_id=P123` - Filter by patient
- `GET /api/consent/audit-events/?action=read` - Filter by action

## Compliance Features

### 1. Data Categories

All form fields must specify a `data_category`:

```json
{
  "fields": [
    {
      "id": "name",
      "label": "Name",
      "type": "text",
      "data_category": "demographics"
    },
    {
      "id": "hba1c",
      "label": "HbA1c",
      "type": "number",
      "data_category": "labs"
    }
  ]
}
```

### 2. Purpose Specification

All forms, rules, and workflows must specify a `purpose`:

```json
{
  "purpose": "treatment",
  "fields": [...],
  "rules": [...]
}
```

### 3. Consent Enforcement

The system enforces consent at multiple levels:

#### Runtime Engine
- Hides fields without read consent
- Blocks form evaluation without valid consent

#### Submission
- Validates consent before saving data
- Returns 403 with guidance if consent missing

#### Clinical Views
- Filters records based on consent
- Logs all access attempts

#### Orchestrator
- Skips PHI-sharing steps without consent
- Creates audit events for workflow decisions

### 4. Audit Trail

Every data access operation is logged with:
- Request ID for traceability
- User and patient context
- Action performed (read/write/share)
- Data categories involved
- Consent decision and reason
- Hash chain for integrity

## Configuration

### Settings

Add to `settings.py`:

```python
INSTALLED_APPS = [
    # ... other apps
    "consent",
]

MIDDLEWARE = [
    # ... other middleware
    "consent.audit_middleware.AuditMiddleware",
]
```

### ABDM Configuration

```python
# settings.py
ABDM_BASE_URL = "https://abdm-sandbox.gov.in"
ABDM_API_KEY = "your_api_key"
ABDM_SECRET_KEY = "your_secret_key"
```

## Usage Examples

### 1. Creating Consent

```python
from consent.models import Consent
from django.utils import timezone
from datetime import timedelta

consent = Consent.objects.create(
    tenant_id="TENANT_A",
    patient_id="P123",
    purpose="treatment",
    data_categories=["demographics", "vitals", "labs"],
    date_range_start=timezone.now(),
    date_range_end=timezone.now() + timedelta(days=365),
    expiry=timezone.now() + timedelta(days=365),
    status="granted"
)
```

### 2. Checking Consent

```python
from consent.utils import check_consent_for_request

result = check_consent_for_request(
    request=request,
    patient_id="P123",
    purpose="treatment",
    data_categories=["demographics", "vitals"]
)

if result['allow']:
    # Proceed with operation
    pass
else:
    # Handle consent denial
    return Response({"error": result['reason']}, status=403)
```

### 3. ABDM Integration

```python
from consent.abdm_connector import abdm_connector

# Create consent request
request = abdm_connector.request_consent(
    patient_id="P123",
    purpose="treatment",
    data_categories=["demographics", "vitals"],
    tenant_id="TENANT_A"
)

# Handle notification
abdm_connector.notify_consent_response(
    request_id=request.abdm_request_id,
    status="granted",
    artefact_id="ARTEFACT_123"
)
```

## Testing

### Seed Test Data

```bash
python manage.py seed_consent_data
```

### Run Tests

```bash
python test_consent_system.py
```

### Test Scenarios

1. **Valid Consent**: Patient with valid consent can access data
2. **No Consent**: Patient without consent gets 403 error
3. **Expired Consent**: Patient with expired consent gets 403 error
4. **Revoked Consent**: Patient with revoked consent gets 403 error
5. **Partial Consent**: Patient with consent for some data categories only
6. **ABDM Flow**: Complete ABDM consent request lifecycle
7. **Audit Logging**: Verify all operations are logged

## DPDP Compliance

### Data Categories

- `demographics`: Name, age, gender, contact info
- `vitals`: Height, weight, BMI, blood pressure
- `labs`: Lab results, HbA1c, blood tests
- `diagnosis`: Medical conditions, diagnoses
- `medications`: Prescribed medications
- `procedures`: Medical procedures, surgeries
- `allergies`: Known allergies
- `family_history`: Family medical history
- `social_history`: Lifestyle, habits
- `insurance`: Insurance information
- `billing`: Billing and payment data
- `images`: Medical images, X-rays
- `documents`: Medical documents, reports

### Purposes

- `treatment`: Direct patient care
- `ops`: Hospital operations
- `research`: Medical research
- `analytics`: Data analytics
- `marketing`: Marketing communications
- `emergency`: Emergency situations

## ABDM Integration

### Consent Request Flow

1. **Initiate**: Create consent request via ABDM
2. **Notify**: Receive notification when patient responds
3. **Fetch**: Retrieve consent artefact
4. **Store**: Link artefact to consent record

### Webhook Handling

The system handles ABDM webhooks for:
- Consent granted/denied notifications
- Consent expiry alerts
- Consent revocation notifications

## Security Features

### Hash Chain Integrity

Each audit event includes a hash of the previous event, creating an immutable chain:

```python
def _generate_hash(self):
    payload = {
        'timestamp': self.timestamp.isoformat(),
        'request_id': self.request_id,
        # ... other fields
    }
    
    payload_str = json.dumps(payload, sort_keys=True)
    if self.previous_hash:
        payload_str = self.previous_hash + payload_str
    
    return hashlib.sha256(payload_str.encode()).hexdigest()
```

### Tenant Isolation

All consent and audit data is isolated by tenant:
- Consent records are tenant-scoped
- Audit events include tenant context
- Cross-tenant access is prevented

### RBAC Integration

Consent checking integrates with existing RBAC:
- Final decision = RBAC ∧ Consent (deny-overrides)
- Field-level permissions respect consent
- Workflow permissions consider consent

## Monitoring and Alerts

### Audit Dashboard

Monitor consent compliance:
- Consent grant/revoke rates
- Access denied events
- Data category usage
- Purpose distribution

### Alerts

Set up alerts for:
- High consent denial rates
- Unusual access patterns
- Consent expiry warnings
- Audit chain integrity issues

## Migration Guide

### From Existing System

1. **Add Data Categories**: Update all form fields with `data_category`
2. **Add Purposes**: Update all specs with `purpose` field
3. **Migrate Consents**: Import existing consent data
4. **Enable Enforcement**: Deploy with consent enforcement enabled
5. **Train Users**: Educate users on consent requirements

### Database Migration

```bash
python manage.py makemigrations consent
python manage.py migrate
```

## Troubleshooting

### Common Issues

1. **Consent Not Found**: Check patient ID and tenant context
2. **Data Category Mismatch**: Verify field data categories match consent
3. **Purpose Mismatch**: Ensure purpose matches consent purpose
4. **Audit Hash Mismatch**: Check for data corruption in audit chain

### Debug Commands

```bash
# Check consent status
python manage.py shell
>>> from consent.models import Consent
>>> Consent.objects.filter(patient_id="P123")

# Verify audit chain
>>> from consent.models import AuditEvent
>>> events = AuditEvent.objects.filter(tenant_id="TENANT_A").order_by('timestamp')
>>> for event in events:
...     print(f"{event.timestamp}: {event.action} - {event.decision}")
```

## Future Enhancements

1. **Consent Templates**: Pre-defined consent templates
2. **Consent Analytics**: Advanced consent analytics
3. **Consent Notifications**: Patient consent notifications
4. **Consent Renewal**: Automated consent renewal workflows
5. **Consent Portability**: Export/import consent data
6. **Consent Verification**: Third-party consent verification

## Support

For issues or questions:
1. Check audit logs for consent decisions
2. Verify tenant context and user permissions
3. Review consent validity and data categories
4. Contact system administrator for assistance
