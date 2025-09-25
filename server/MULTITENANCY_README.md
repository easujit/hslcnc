# Multi-Tenancy Implementation

This document describes the comprehensive multi-tenancy system implemented in the Django+DRF POC.

## Overview

The multi-tenancy system provides:
- **Tenant Isolation**: Complete data separation between tenants
- **Quota Management**: Rate limiting and usage tracking per tenant
- **Tenant Context**: Thread-local tenant context management
- **RBAC Integration**: Role-based access control per tenant
- **API Security**: Tenant validation on all endpoints

## Architecture

### Core Components

1. **Core Module** (`core/`)
   - `tenant.py`: Thread-local tenant context management
   - `middleware.py`: Tenant extraction from JWT/headers
   - `models.py`: AbstractTenantModel and TenantManager
   - `drf_mixins.py`: DRF view mixins for tenant scoping

2. **Quotas Module** (`quotas/`)
   - `models.py`: TenantQuota and TenantUsage models
   - `rate_limiting.py`: Token bucket rate limiter

3. **Updated Models**
   - All models now inherit from `AbstractTenantModel`
   - `tenant_id` field added to all multi-tenant models
   - Composite unique constraints for tenant isolation

## Tenant Context

### Thread-Local Storage

```python
from core.tenant import set_current_tenant, get_current_tenant, require_tenant

# Set tenant context
set_current_tenant('TENANT_123')

# Get current tenant
tenant_id = get_current_tenant()

# Require tenant (raises exception if not set)
tenant_id = require_tenant()
```

### Middleware

The `TenantContextMiddleware` extracts tenant information from:

1. **JWT Token** (primary): `Authorization: Bearer <token>`
   - Decodes JWT and extracts `tenant_id` claim
   - Falls back to header if JWT parsing fails

2. **X-Tenant Header** (DEBUG mode only):
   - `X-Tenant: TENANT_123`
   - Only works when `DEBUG=True`

### Tenant Validation

All API endpoints now require tenant context:
- Missing tenant → 401 "Tenant context required"
- Invalid tenant → 401 "no tenant"

## Data Isolation

### AbstractTenantModel

All multi-tenant models inherit from `AbstractTenantModel`:

```python
class Patient(AbstractTenantModel):
    external_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    
    class Meta:
        unique_together = ('tenant_id', 'external_id')
```

### TenantManager

Automatic tenant filtering:

```python
# Only returns objects for current tenant
patients = Patient.objects.all()

# Creates objects with current tenant_id
patient = Patient.objects.create(name="John")
```

### Database Constraints

- **Composite Uniques**: `(tenant_id, external_id)` for patient uniqueness
- **Indexes**: `(tenant_id, created_at)` for performance
- **Foreign Keys**: Maintained within tenant scope

## Rate Limiting & Quotas

### Token Bucket Algorithm

```python
from quotas.rate_limiting import tenant_limited

@tenant_limited(metric="submit", rate=60, burst=30)
def submit_visit_opd(request):
    # Rate limited to 60 requests/minute with burst of 30
    pass
```

### Quota Configuration

```python
# Create tenant quotas
quota = TenantQuota.objects.create(
    tenant_id='TENANT_123',
    limits_json={
        'submit': {
            'rate_per_minute': 100,
            'burst': 50
        },
        'process': {
            'rate_per_minute': 30,
            'burst': 10
        }
    }
)
```

### Usage Tracking

```python
# Track usage
usage = TenantUsage.get_current_usage('TENANT_123', 'submit', 'minute')
usage.increment(1)
```

## API Changes

### Updated Endpoints

All endpoints now:
1. Require tenant context
2. Filter data by tenant
3. Apply rate limiting where appropriate

### Example: Visit Submission

```bash
# Before (no tenant)
curl -X POST /api/submission/submit-visit-opd/ \
  -H "Content-Type: application/json" \
  -d '{"external_id": "P001", "name": "John"}'

# After (with tenant)
curl -X POST /api/submission/submit-visit-opd/ \
  -H "Content-Type: application/json" \
  -H "X-Tenant: TENANT_123" \
  -d '{"external_id": "P001", "name": "John"}'
```

### Rate Limiting Responses

```json
{
  "error": "rate limit",
  "message": "Rate limit exceeded for submit",
  "quota_info": {
    "metric": "submit",
    "rate_per_minute": 60,
    "burst": 30,
    "is_allowed": false
  }
}
```

## RBAC Integration

### Tenant-Scoped Policies

RBAC policies are now tenant-scoped:

```python
# Policy rules are filtered by tenant_id
policies = PolicyRule.objects.filter(tenant_id=current_tenant)
```

### Field-Level Permissions

Field access is controlled per tenant:

```python
# Only returns fields user can access for current tenant
authorized_fields = get_authorized_fields(user_claims, form_name, fields)
```

## Migration Strategy

### Data Migration

Existing data is migrated with a default tenant:

```python
# Run migration script
python migrate_tenant_data.py
```

This sets `tenant_id='DEV'` for all existing records.

### Database Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

## Testing

### Unit Tests

```python
# Test tenant isolation
def test_tenant_isolation():
    set_current_tenant('TENANT_A')
    patient_a = Patient.objects.create(name="Patient A")
    
    set_current_tenant('TENANT_B')
    patient_b = Patient.objects.create(name="Patient B")
    
    # Verify isolation
    assert Patient.objects.count() == 1  # Only current tenant's data
```

### Integration Tests

```python
# Test API with tenant headers
def test_api_tenant_isolation():
    headers = {'X-Tenant': 'TENANT_123'}
    response = requests.get('/api/clinical/patients/', headers=headers)
    assert response.status_code == 200
```

### Rate Limiting Tests

```python
# Test rate limiting
def test_rate_limiting():
    for i in range(100):  # Exceed rate limit
        response = requests.post('/api/submit/', headers=tenant_headers)
        if i > 60:
            assert response.status_code == 429
```

## Configuration

### Settings

```python
# settings.py
INSTALLED_APPS = [
    'core',
    'quotas',
    # ... other apps
]

MIDDLEWARE = [
    # ... other middleware
    'core.middleware.TenantContextMiddleware',
    'policies.middleware.ClaimsMiddleware',
]
```

### Environment Variables

```bash
# JWT secret for tenant extraction
JWT_SECRET_KEY=your-secret-key

# Rate limiting backend (memory or redis)
RATE_LIMIT_BACKEND=memory
```

## Security Considerations

### Tenant Validation

- All API endpoints validate tenant context
- Database queries are automatically scoped to tenant
- No cross-tenant data leakage possible

### Rate Limiting

- Per-tenant rate limits prevent abuse
- Token bucket algorithm allows burst traffic
- Configurable limits per tenant

### RBAC Integration

- Policies are tenant-scoped
- Field-level permissions per tenant
- Workflow permissions per tenant

## Monitoring & Observability

### Usage Metrics

```python
# Get tenant usage
usage = TenantUsage.objects.filter(
    tenant_id='TENANT_123',
    period='day'
).order_by('-window_start')

# Get quota limits
quota = TenantQuota.objects.get(tenant_id='TENANT_123')
limits = quota.get_limit('submit')
```

### Rate Limit Monitoring

```python
# Check rate limit status
is_allowed, info = rate_limiter.check_quota('TENANT_123', 'submit')
print(f"Allowed: {is_allowed}, Info: {info}")
```

## Troubleshooting

### Common Issues

1. **401 "Tenant context required"**
   - Ensure `X-Tenant` header is set
   - Check middleware configuration
   - Verify JWT token has `tenant_id` claim

2. **Empty data in API responses**
   - Check tenant context is set correctly
   - Verify data exists for current tenant
   - Check RBAC policies

3. **429 Rate limit exceeded**
   - Check quota configuration
   - Verify rate limiting is working
   - Consider increasing limits

### Debug Commands

```python
# Check current tenant
from core.tenant import get_current_tenant
print(f"Current tenant: {get_current_tenant()}")

# Check tenant data
from clinical.models import Patient
print(f"Patient count: {Patient.objects.count()}")

# Check rate limits
from quotas.rate_limiting import rate_limiter
is_allowed, info = rate_limiter.check_quota('TENANT_123', 'submit')
print(f"Rate limit: {is_allowed}, {info}")
```

## Future Enhancements

### Planned Features

1. **Tenant Management UI**: Admin interface for managing tenants
2. **Dynamic Quotas**: Runtime quota adjustment
3. **Tenant Analytics**: Usage dashboards per tenant
4. **Tenant Onboarding**: Automated tenant setup
5. **Cross-Tenant Reporting**: Aggregated analytics (with proper permissions)

### Performance Optimizations

1. **Tenant Caching**: Cache tenant-specific data
2. **Database Partitioning**: Partition tables by tenant
3. **Connection Pooling**: Tenant-aware connection pools
4. **Query Optimization**: Tenant-specific query optimization

## Conclusion

The multi-tenancy system provides comprehensive tenant isolation, quota management, and security while maintaining the existing functionality. All data is properly isolated, and the system scales to support multiple tenants with different access patterns and rate limits.
