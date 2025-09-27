# 🧪 UI Testing Guide for Consent Management System

## **Prerequisites**

1. **Start Backend Server:**
   ```bash
   cd D:\lCNC_POC\new\server
   python manage.py runserver
   ```

2. **Start Frontend Server:**
   ```bash
   cd D:\lCNC_POC\new\client
   npm run dev
   ```

3. **Seed Test Data:**
   ```bash
   cd D:\lCNC_POC\new\server
   python manage.py seed_consent_data
   ```

4. **Access Application:**
   Open browser to `http://localhost:5173`

## **🎯 Test Scenarios**

### **Test 1: Consent Management UI**

1. **Navigate to Consent Management**
   - Click "Consent Management" in the navigation
   - You should see a list of existing consents

2. **Create New Consent**
   - Click "Create New Consent" button
   - Fill out the form:
     - Patient ID: Select from dropdown (P123, P456, P789, P999)
     - Purpose: Select "treatment"
     - Data Categories: Check "demographics", "vitals", "labs"
     - Leave dates as default (1 year from now)
   - Click "Create Consent"
   - Verify consent appears in the list

3. **Test Consent Actions**
   - Click "Check" button on any consent
   - Verify consent check result dialog
   - Click "Revoke" on a granted consent
   - Verify status changes to "revoked"

### **Test 2: Form Submission with Valid Consent**

1. **Navigate to Visit Page**
   - Click "Visit" in navigation

2. **Test Patient P123 (Has Valid Consent)**
   - Patient ID: `P123`
   - Name: `John Doe`
   - Age: `45`
   - Height: `175`
   - Weight: `80`
   - HbA1c: `8.5`
   - Click "Save Visit"

3. **Expected Result:**
   - Form should save successfully
   - You should see success message
   - Visit should appear in Visit History

### **Test 3: Form Submission without Consent**

1. **Test Patient P999 (Has Revoked Consent)**
   - Patient ID: `P999`
   - Name: `Jane Doe`
   - Age: `35`
   - Height: `165`
   - Weight: `60`
   - HbA1c: `7.2`
   - Click "Save Visit"

2. **Expected Result:**
   - Should get 403 error
   - Error message: "Consent required: [reason]"
   - Form should not save

### **Test 4: Form Submission with Expired Consent**

1. **Test Patient P789 (Has Expired Consent)**
   - Patient ID: `P789`
   - Name: `Bob Smith`
   - Age: `30`
   - Height: `180`
   - Weight: `75`
   - HbA1c: `6.8`
   - Click "Save Visit"

2. **Expected Result:**
   - Should get 403 error
   - Error message: "Consent required: No valid consent found"
   - Form should not save

### **Test 5: Field Visibility Based on Consent**

1. **Test Patient P456 (Has Research Consent Only)**
   - Patient ID: `P456`
   - Name: `Alice Johnson`
   - Age: `28`
   - Height: `160`
   - Weight: `55`
   - HbA1c: `5.9`

2. **Expected Result:**
   - Some fields might be hidden based on consent
   - Form might show error or limited functionality

### **Test 6: Multi-Tenant Consent Isolation**

1. **Switch Tenant Context**
   - Use Tenant Switcher in top-right corner
   - Switch from "TENANT_A" to "TENANT_B"

2. **Test Same Patient ID**
   - Patient ID: `P123` (same ID, different tenant)
   - Fill out form with same data

3. **Expected Result:**
   - Should work if TENANT_B has consent for P123
   - Should fail if TENANT_B doesn't have consent for P123

### **Test 7: Workflow Consent Enforcement**

1. **Submit Visit with HbA1c >= 9**
   - Patient ID: `P123` (has valid consent)
   - HbA1c: `9.5` (triggers diabetes educator workflow)
   - Click "Save Visit"

2. **Expected Result:**
   - Form should save successfully
   - Check "Notifications" page for diabetes educator notification
   - Check "Tasks" page for diabetes educator task

3. **Test Without Consent**
   - Patient ID: `P999` (no valid consent)
   - HbA1c: `9.5`
   - Click "Save Visit"

4. **Expected Result:**
   - Should get consent error before workflow triggers
   - No notifications or tasks should be created

### **Test 8: Audit Logging**

1. **Perform Various Actions**
   - Submit forms with different patients
   - Access different pages
   - Create/revoke consents

2. **Check Audit Events**
   - Go to Consent Management page
   - Look for audit events in browser developer tools
   - Check backend logs for audit events

### **Test 9: ABDM Integration (Simulated)**

1. **Create ABDM Consent Request**
   - Use browser developer tools or API testing tool
   - POST to `/api/consent/abdm/request-consent/`
   - Body: `{"patient_id": "P200", "purpose": "treatment", "data_categories": ["demographics", "vitals"]}`

2. **Simulate ABDM Notification**
   - POST to `/api/consent/abdm/notify/`
   - Body: `{"request_id": "ABDM_REQ_123", "status": "granted", "artefact_id": "ARTEFACT_123"}`

3. **Expected Result:**
   - Consent request should be created
   - Notification should update request status
   - Consent should be created and linked

### **Test 10: Compliance Linting**

1. **Navigate to Configurator**
   - Click "Configurator" in navigation

2. **Test Form Publishing**
   - Go to "Form" tab
   - Try to publish a form without data categories
   - Expected: Should get compliance error

3. **Test Rules Publishing**
   - Go to "Rules" tab
   - Try to publish rules without purpose
   - Expected: Should get compliance error

4. **Test Workflow Publishing**
   - Go to "Workflow" tab
   - Try to publish workflow without purpose
   - Expected: Should get compliance error

## **🔍 Debugging Tips**

### **Check Browser Console**
- Open Developer Tools (F12)
- Look for API errors in Console tab
- Check Network tab for failed requests

### **Check Backend Logs**
- Look at Django server console
- Check for consent check results
- Look for audit event creation

### **Verify Database**
```bash
cd D:\lCNC_POC\new\server
python manage.py shell
>>> from consent.models import Consent, AuditEvent
>>> Consent.objects.all()
>>> AuditEvent.objects.all()
```

### **Test API Directly**
```bash
# Test consent check
curl -X POST http://localhost:8000/api/consent/consent/check/ \
  -H "Content-Type: application/json" \
  -H "X-Tenant: TENANT_A" \
  -d '{"patient_id": "P123", "purpose": "treatment", "data_categories": ["demographics", "vitals"]}'
```

## **📊 Expected Test Results**

| Test Case | Patient | Expected Result |
|-----------|---------|-----------------|
| Valid Consent | P123 | ✅ Form saves, workflow triggers |
| No Consent | P999 | ❌ 403 error, no save |
| Expired Consent | P789 | ❌ 403 error, no save |
| Research Consent | P456 | ⚠️ Limited access based on purpose |
| Multi-Tenant | P123 (TENANT_B) | Depends on tenant's consent data |

## **🚨 Common Issues**

1. **"Consent required" error on valid patient**
   - Check if consent is expired
   - Verify data categories match
   - Check tenant context

2. **Form saves without consent**
   - Check if consent enforcement is enabled
   - Verify middleware is loaded
   - Check backend logs

3. **Fields not hiding**
   - Check runtime engine consent integration
   - Verify form configuration has data categories
   - Check consent covers required data categories

4. **Workflow not triggering**
   - Check if consent allows PHI sharing
   - Verify orchestrator consent integration
   - Check audit logs for workflow decisions

## **✅ Success Criteria**

- [ ] Consent Management UI loads and functions
- [ ] Can create, view, and revoke consents
- [ ] Form submission respects consent
- [ ] Field visibility based on consent
- [ ] Multi-tenant isolation works
- [ ] Workflow consent enforcement works
- [ ] Audit events are created
- [ ] Compliance linting blocks invalid specs
- [ ] ABDM integration works (simulated)

## **🎉 Completion**

Once all tests pass, you have successfully verified that the Consent Management system is working correctly from the UI! The system now provides:

- **Full DPDP Compliance**: All data access is consent-gated
- **ABDM Integration**: Ready for real ABDM integration
- **Audit Trail**: Complete audit logging
- **Multi-Tenant**: Tenant-isolated consent management
- **UI Integration**: User-friendly consent management interface
