# RBAC (Role-Based Access Control) System

This module implements a comprehensive Role-Based Access Control system with field-level, record-level, and workflow-level permissions for the Hospital POC.

## Features

- **Field-level permissions**: Control read/write/mask access to individual form fields
- **Record-level permissions**: Control access to specific records based on tenant/department
- **Workflow permissions**: Control who can publish workflows and execute workflow steps
- **Default-deny security**: All access is denied by default unless explicitly allowed
- **Deny-overrides**: Deny rules take precedence over allow rules
- **Conditional permissions**: Support for complex conditions using safe expression evaluation
- **Caching**: Policies are cached for 60 seconds for performance

## Models

### PolicyRule
- `tenant_id`: Tenant identifier
- `version`: Policy version number
- `status`: 'draft' or 'published'
- `resource_type`: 'field', 'record', 'workflow', or 'workflow_step'
- `action`: Action being controlled (read, write, execute, publish, etc.)
- `selector`: JSON criteria for matching resources
- `effect`: 'allow' or 'deny'
- `condition`: Optional Python expression for additional conditions

## API Endpoints

### Policy Management
- `GET /api/policies/rules/` - List all policy rules
- `POST /api/policies/rules/` - Create new policy rule
- `PUT /api/policies/rules/{id}/` - Update policy rule
- `DELETE /api/policies/rules/{id}/` - Delete policy rule
- `POST /api/policies/rules/{id}/publish/` - Publish policy rule

### Effective Policies
- `GET /api/policies/effective/` - Get effective policies for current tenant

## Usage

### Field-level Permissions

```python
from policies.authorization import authorize, get_authorized_fields

# Check if user can read a field
can_read = authorize(
    user_claims,
    'field',
    'read',
    {'form': 'visit_opd', 'field': 'hba1c'}
)

# Filter fields based on permissions
authorized_fields = get_authorized_fields(
    user_claims,
    'visit_opd',
    form_fields
)
```

### Record-level Permissions

```python
# Check if user can read a record
can_read = authorize(
    user_claims,
    'record',
    'read',
    {'type': 'visit'},
    record=visit_data
)
```

### Workflow Permissions

```python
# Check if user can publish workflow
can_publish = authorize(
    user_claims,
    'workflow',
    'publish',
    {'workflow': 'visit_opd'}
)

# Check if user can execute workflow step
can_execute = authorize(
    user_claims,
    'workflow_step',
    'execute',
    {'workflow': 'visit_opd', 'step': 'diabetes_educator'}
)
```

## Middleware

The `ClaimsMiddleware` extracts user claims from HTTP headers:
- `X-Tenant`: Tenant ID
- `X-Roles`: Comma-separated list of roles
- `X-Departments`: Comma-separated list of departments
- `X-User-ID`: User identifier
- `X-Username`: Username

## Condition Expressions

Conditions support safe Python expressions with:
- Basic operators: `and`, `or`, `==`, `!=`, `in`, `not in`
- Attribute access: `user.roles`, `record.custom_data`
- List operations: `'Doctor' in user.roles`
- Dictionary access: `record.custom_data.get('tenant_id')`

## Sample Policies

### Field Permissions
```json
{
  "tenant_id": "H001",
  "resource_type": "field",
  "action": "read",
  "selector": {"form": "visit_opd", "field": "hba1c"},
  "effect": "allow",
  "condition": "'Doctor' in user.roles or 'Nurse' in user.roles"
}
```

### Record Permissions
```json
{
  "tenant_id": "H001",
  "resource_type": "record",
  "action": "read",
  "selector": {"type": "visit"},
  "effect": "allow",
  "condition": "user.tenant_id == record.custom_data.get('tenant_id', 'H001')"
}
```

### Workflow Permissions
```json
{
  "tenant_id": "H001",
  "resource_type": "workflow",
  "action": "publish",
  "selector": {"workflow": "visit_opd"},
  "effect": "allow",
  "condition": "'ClinicalLead' in user.roles or 'Admin' in user.roles"
}
```

## Security

- **Default Deny**: All access is denied unless explicitly allowed
- **Deny Overrides**: Deny rules always take precedence over allow rules
- **Safe Evaluation**: Condition expressions are evaluated in a restricted environment
- **Caching**: Policies are cached to prevent repeated database queries
- **Audit Trail**: All policy changes are tracked with timestamps

## Testing

Run the test suite:
```bash
python manage.py test policies
```

## Seeding Policies

Seed default policies:
```bash
python manage.py seed_policies
```
