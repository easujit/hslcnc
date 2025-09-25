# Extensions API - Hospital POC

This module provides a comprehensive extension system for the Hospital POC, allowing external developers to plug in custom logic safely through HTTP webhooks and API calls.

## Overview

The Extensions API enables:
- **Runtime Extensions**: Custom calculations and validations during form processing
- **Submission Hooks**: Pre and post-submission processing
- **Event Subscriptions**: Real-time event delivery to external systems
- **Workflow Webhooks**: Configurable webhook actions in workflows
- **Dead Letter Queue**: Failed message handling and retry mechanisms

## Models

### ExtensionFunction
Runtime extensions for compute and validation operations.

```json
{
  "name": "bmi_calculator",
  "type": "runtime.compute",
  "match_json": {"form": "visit_opd"},
  "invoke_json": {
    "method": "POST",
    "url": "https://api.example.com/bmi",
    "timeout_ms": 1000,
    "headers": {"Authorization": "Bearer token"}
  },
  "secret": "hmac-secret-key",
  "retries": 3,
  "cache_ttl_s": 300,
  "is_blocking": false,
  "enabled": true
}
```

### ExtensionHook
Submission hooks for pre/post processing.

```json
{
  "name": "age_validation",
  "phase": "submission.pre",
  "match_json": {"age": {"$lt": 18}},
  "invoke_json": {
    "method": "POST",
    "url": "https://api.example.com/validate",
    "timeout_ms": 2000
  },
  "secret": "hmac-secret-key",
  "retries": 2,
  "is_blocking": true,
  "enabled": true
}
```

### ExtSubscription
Event subscriptions for external systems.

```json
{
  "name": "external_system",
  "topics": ["visit_saved", "patient_created"],
  "endpoint": "https://api.example.com/webhook",
  "secret": "hmac-secret-key",
  "retries": 3,
  "dead_letter": true,
  "enabled": true
}
```

### DeadLetter
Failed message queue for retry handling.

```json
{
  "kind": "hook",
  "target": "https://api.example.com/failed",
  "payload_json": {"event": "visit_saved", "data": {...}},
  "last_error": "Connection timeout",
  "retry_count": 2
}
```

## API Endpoints

### Extension Functions
- `GET /api/ext/functions/` - List all extension functions
- `POST /api/ext/functions/` - Create new extension function
- `PUT /api/ext/functions/{id}/` - Update extension function
- `DELETE /api/ext/functions/{id}/` - Delete extension function

### Extension Hooks
- `GET /api/ext/hooks/` - List all extension hooks
- `POST /api/ext/hooks/` - Create new extension hook
- `PUT /api/ext/hooks/{id}/` - Update extension hook
- `DELETE /api/ext/hooks/{id}/` - Delete extension hook

### Event Subscriptions
- `GET /api/ext/subscriptions/` - List all subscriptions
- `POST /api/ext/subscriptions/` - Create new subscription
- `PUT /api/ext/subscriptions/{id}/` - Update subscription
- `DELETE /api/ext/subscriptions/{id}/` - Delete subscription

### Dead Letter Queue
- `GET /api/ext/dead-letters/` - List all dead letters
- `POST /api/ext/dead-letters/{id}/retry/` - Retry dead letter

## Security

### HMAC Signatures
All webhook calls are signed with HMAC-SHA256:

```
X-Hook-Signature: sha256=<hex>
X-Hook-Timestamp: <unix_timestamp>
```

### Signature Verification
```python
import hmac
import hashlib
import json

def verify_signature(payload, signature, secret):
    payload_str = json.dumps(payload, sort_keys=True, separators=(',', ':'))
    expected = hmac.new(
        secret.encode('utf-8'),
        payload_str.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, f"sha256={expected}")
```

## Integration Points

### Runtime Engine
Extension functions are called during rule evaluation:

```python
# Extension function response format
{
  "setField": [
    {"id": "bmi", "value": 25.5}
  ],
  "visibility": [
    {"id": "risk_warning", "visible": true}
  ],
  "warnings": ["BMI calculated externally"],
  "errors": []
}
```

### Submission Process
Pre-hooks can block submission, post-hooks run best-effort:

```python
# Pre-hook can block submission
if hook.is_blocking and not success:
    return Response({"error": "Validation failed"}, status=400)

# Post-hook failures go to dead letter queue
if not success:
    DeadLetter.objects.create(
        kind='hook',
        target=url,
        payload_json=payload,
        last_error=error_msg
    )
```

### Orchestrator
Event subscriptions receive all outbox events:

```python
# Event payload format
{
  "topic": "visit_saved",
  "payload": {"visit_id": 123, "patient_name": "John"},
  "timestamp": "2024-01-01T12:00:00Z",
  "event_id": 456
}
```

## Workflow Webhooks

Add webhook actions to workflow configurations:

```json
{
  "post_save": [
    {"emit": "visit_saved"},
    {
      "webhook": {
        "url": "https://api.example.com/notify",
        "method": "POST",
        "timeout_ms": 1200,
        "retries": 3,
        "body": {"custom_field": "value"}
      }
    }
  ]
}
```

## Error Handling

### Timeouts
- Runtime extensions: Max 1200ms
- Submission hooks: Configurable (default 5000ms)
- Event subscriptions: 5000ms
- Workflow webhooks: Configurable (default 1200ms)

### Retries
- Exponential backoff with max 10 second delay
- Configurable retry counts per extension
- Failed messages go to dead letter queue

### Dead Letter Queue
- Automatic retry mechanism
- Manual retry via API
- Error tracking and logging

## Usage Examples

### 1. BMI Calculator Extension
```bash
# Create extension function
curl -X POST http://localhost:8000/api/ext/functions/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "bmi_calculator",
    "type": "runtime.compute",
    "match_json": {"form": "visit_opd"},
    "invoke_json": {
      "method": "POST",
      "url": "https://api.example.com/bmi",
      "timeout_ms": 1000
    },
    "secret": "your-secret-key",
    "retries": 3,
    "is_blocking": false,
    "enabled": true
  }'
```

### 2. Age Validation Hook
```bash
# Create pre-submission hook
curl -X POST http://localhost:8000/api/ext/hooks/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "age_validation",
    "phase": "submission.pre",
    "match_json": {"age": {"$lt": 18}},
    "invoke_json": {
      "method": "POST",
      "url": "https://api.example.com/validate-age",
      "timeout_ms": 2000
    },
    "secret": "your-secret-key",
    "retries": 2,
    "is_blocking": true,
    "enabled": true
  }'
```

### 3. Event Subscription
```bash
# Create event subscription
curl -X POST http://localhost:8000/api/ext/subscriptions/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "external_system",
    "topics": ["visit_saved"],
    "endpoint": "https://api.example.com/webhook",
    "secret": "your-secret-key",
    "retries": 3,
    "dead_letter": true,
    "enabled": true
  }'
```

## Testing

Run the test suite:
```bash
python manage.py test extensions
```

The tests cover:
- Model creation and validation
- HMAC signature generation/verification
- Criteria matching logic
- Integration with runtime engine
- Dead letter queue functionality

## Monitoring

### Dead Letter Queue
Monitor failed messages:
```bash
curl http://localhost:8000/api/ext/dead-letters/
```

### Extension Status
Check extension health through logs and dead letter queue.

### Performance
- Monitor response times in logs
- Track retry counts in dead letter queue
- Set up alerts for high failure rates

## Best Practices

1. **Security**: Always use HMAC signatures for webhook authentication
2. **Timeouts**: Set appropriate timeouts based on your service capabilities
3. **Retries**: Configure retry counts based on service reliability
4. **Monitoring**: Set up monitoring for dead letter queue and extension health
5. **Testing**: Test extensions thoroughly before enabling in production
6. **Error Handling**: Implement proper error handling in your extension endpoints
7. **Idempotency**: Make your extensions idempotent to handle retries safely

## Troubleshooting

### Common Issues

1. **Extension not called**: Check match criteria and enabled status
2. **HMAC verification fails**: Verify secret key and payload format
3. **Timeouts**: Increase timeout values or optimize your service
4. **Dead letters**: Check endpoint availability and error logs
5. **Blocking hooks**: Ensure pre-hooks don't block legitimate submissions

### Debug Mode
Enable debug logging to see extension calls:
```python
import logging
logging.getLogger('extensions').setLevel(logging.DEBUG)
```
