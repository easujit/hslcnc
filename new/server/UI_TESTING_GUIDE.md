# Multi-Tenancy UI Testing Guide

This guide shows you how to test the multi-tenancy system from the UI.

## Prerequisites

1. **Backend Server Running**:
   ```bash
   cd server
   python manage.py runserver
   ```

2. **Frontend Server Running**:
   ```bash
   cd client
   npm run dev
   ```

## Testing Multi-Tenancy from UI

### Method 1: Using Browser Developer Tools

1. **Open Browser Developer Tools** (F12)
2. **Go to Network Tab**
3. **Navigate to the application** (http://localhost:5173)
4. **Intercept and Modify Requests**:

#### Test 1: Visit Page with Different Tenants

1. Go to **Visit** page
2. Open Developer Tools → Network tab
3. Fill out the form and click "Save Visit"
4. **Before the request is sent**, right-click on the request → "Edit and Resend"
5. **Add tenant headers**:
   ```
   X-Tenant: TENANT_A
   X-Roles: Doctor
   X-Departments: Endocrinology
   ```
6. **Send the request**
7. **Repeat with different tenant**:
   ```
   X-Tenant: TENANT_B
   X-Roles: Nurse
   X-Departments: Cardiology
   ```

#### Test 2: Visit History Isolation

1. Go to **Visit History** page
2. **Modify the request** to add tenant headers
3. **Verify** that only visits for that tenant are shown
4. **Switch tenants** and verify data isolation

#### Test 3: Configurator Tenant Isolation

1. Go to **Configurator** page
2. **Add tenant headers** to all requests
3. **Create/modify forms** for different tenants
4. **Verify** that each tenant only sees their own configurations

### Method 2: Using Browser Extensions

#### ModHeader Extension (Recommended)

1. **Install ModHeader** browser extension
2. **Add headers**:
   - `X-Tenant`: `TENANT_A`
   - `X-Roles`: `Doctor`
   - `X-Departments`: `Endocrinology`
3. **Navigate through the application**
4. **Switch tenants** by changing the header values

#### Requestly Extension

1. **Install Requestly** browser extension
2. **Create rules** to add headers to all requests
3. **Test different tenant combinations**

### Method 3: Using Postman/Insomnia

1. **Import the API collection** (if available)
2. **Set default headers**:
   ```
   X-Tenant: TENANT_A
   X-Roles: Doctor
   X-Departments: Endocrinology
   ```
3. **Test all endpoints** with different tenant values

## Test Scenarios

### Scenario 1: Tenant Isolation

**Objective**: Verify that tenants cannot see each other's data

**Steps**:
1. **Create data for Tenant A**:
   - Set `X-Tenant: TENANT_A`
   - Create a patient: "John Doe" with ID "P001"
   - Submit a visit with HbA1c = 8.5

2. **Create data for Tenant B**:
   - Set `X-Tenant: TENANT_B`
   - Create a patient: "Jane Smith" with ID "P002"
   - Submit a visit with HbA1c = 9.2

3. **Verify isolation**:
   - Switch to Tenant A → Should only see John Doe's data
   - Switch to Tenant B → Should only see Jane Smith's data

**Expected Result**: Complete data isolation between tenants

### Scenario 2: Rate Limiting

**Objective**: Test rate limiting per tenant

**Steps**:
1. **Set tenant headers** for Tenant A
2. **Rapidly submit multiple visits** (more than 60 in a minute)
3. **Observe rate limiting**:
   - First 60 requests should succeed
   - Subsequent requests should return 429 "rate limit"

4. **Test different tenant**:
   - Set headers for Tenant B
   - Should have separate rate limit bucket

**Expected Result**: Rate limiting works per tenant independently

### Scenario 3: RBAC with Multi-Tenancy

**Objective**: Test role-based access control with tenant isolation

**Steps**:
1. **Test Doctor role**:
   - Set `X-Tenant: TENANT_A`, `X-Roles: Doctor`
   - Should see all fields and records

2. **Test Nurse role**:
   - Set `X-Tenant: TENANT_A`, `X-Roles: Nurse`
   - Should see limited fields (no HbA1c)

3. **Test Clerk role**:
   - Set `X-Tenant: TENANT_A`, `X-Roles: Clerk`
   - Should see only basic fields

4. **Test cross-tenant access**:
   - Set `X-Tenant: TENANT_B`, `X-Roles: Doctor`
   - Should not see Tenant A's data

**Expected Result**: RBAC works within tenant boundaries

### Scenario 4: Workflow Execution

**Objective**: Test workflow execution with tenant isolation

**Steps**:
1. **Set tenant headers** for Tenant A
2. **Submit visit** with HbA1c >= 9
3. **Check Tasks/Notifications**:
   - Should see diabetes educator task
   - Should see notification

4. **Test different tenant**:
   - Set headers for Tenant B
   - Submit visit with HbA1c >= 9
   - Should see separate tasks/notifications

**Expected Result**: Workflows execute per tenant independently

## Testing Tools

### Browser Developer Tools

**Chrome/Edge**:
1. F12 → Network tab
2. Right-click request → "Edit and Resend"
3. Add headers in "Request Headers" section

**Firefox**:
1. F12 → Network tab
2. Right-click request → "Edit and Resend"
3. Add headers in "Request Headers" section

### Browser Extensions

**ModHeader**:
- Add persistent headers to all requests
- Easy tenant switching
- Available for Chrome, Firefox, Edge

**Requestly**:
- Advanced request modification
- Rule-based header injection
- Available for Chrome, Firefox, Edge

### API Testing Tools

**Postman**:
- Set default headers for all requests
- Environment variables for tenant switching
- Collection sharing

**Insomnia**:
- Similar to Postman
- Good for API testing

## Common Issues & Solutions

### Issue 1: 401 "Tenant context required"

**Cause**: Missing `X-Tenant` header
**Solution**: Add `X-Tenant: TENANT_NAME` header to requests

### Issue 2: Empty data in responses

**Cause**: No data exists for current tenant
**Solution**: 
1. Check if data was created for the correct tenant
2. Verify tenant headers are set correctly
3. Check if migrations were applied

### Issue 3: 429 Rate limit exceeded

**Cause**: Exceeded rate limit for tenant
**Solution**: 
1. Wait for rate limit to reset
2. Check quota configuration
3. Use different tenant for testing

### Issue 4: RBAC not working

**Cause**: Policies not created for tenant
**Solution**:
1. Run `python seed_rbac_policies.py` for the tenant
2. Check policy configuration
3. Verify tenant headers are correct

## Verification Checklist

- [ ] **Tenant Isolation**: Data is completely separated between tenants
- [ ] **Rate Limiting**: Each tenant has independent rate limits
- [ ] **RBAC**: Role-based access works within tenant boundaries
- [ ] **Workflows**: Tasks and notifications are tenant-specific
- [ ] **API Security**: All endpoints require tenant context
- [ ] **Data Integrity**: No cross-tenant data leakage
- [ ] **Performance**: Queries are optimized with proper indexing

## Advanced Testing

### Load Testing

**Tools**: JMeter, Artillery, k6
**Scenario**: Multiple tenants with high request volume
**Focus**: Rate limiting, database performance, memory usage

### Security Testing

**Tools**: OWASP ZAP, Burp Suite
**Scenario**: Attempt cross-tenant data access
**Focus**: Authorization bypass, data leakage

### Integration Testing

**Tools**: Selenium, Playwright
**Scenario**: End-to-end user workflows
**Focus**: Complete user journeys with tenant switching

## Conclusion

The multi-tenancy system provides complete tenant isolation with robust security and performance features. Use this guide to thoroughly test all aspects of the system and ensure it meets your requirements.
