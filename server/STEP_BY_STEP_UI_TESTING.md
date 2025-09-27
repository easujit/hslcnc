# Step-by-Step UI Testing Guide for Multi-Tenancy

This guide will walk you through testing the multi-tenancy system from the UI.

## Prerequisites

Make sure you have both servers running:

### 1. Start Backend Server
```bash
cd server
python manage.py runserver
```
**Expected**: Server starts on http://localhost:8000

### 2. Start Frontend Server
```bash
cd client
npm run dev
```
**Expected**: Frontend starts on http://localhost:5173

## Step 1: Access the Application

1. **Open your browser** and go to `http://localhost:5173`
2. **Look for the Tenant Switcher** in the top-right corner of the header
3. **You should see**: A button showing "HOSPITAL A" with "👨‍⚕️ Doctor" and a dropdown arrow

## Step 2: Test Tenant Switching

### Switch to Different Tenants

1. **Click the Tenant Switcher** button
2. **Select "Hospital B"** from the dropdown
3. **Notice**: The page reloads and the switcher now shows "HOSPITAL B"
4. **Switch to "Clinic C"** and verify the change

### Switch Roles

1. **Click the Tenant Switcher** again
2. **In the Role section**, select "Nurse"
3. **Notice**: The page reloads and shows "👩‍⚕️ Nurse"
4. **Try "Clerk"** role and verify the change

## Step 3: Test Data Isolation

### Create Data for Tenant A

1. **Set tenant to "Hospital A"** and role to "Doctor"
2. **Go to Visit page**
3. **Fill out the form**:
   - Patient ID: `PATIENT_A_001`
   - Name: `John Doe`
   - Age: `35`
   - Height: `175`
   - Weight: `80`
   - HbA1c: `8.5`
4. **Click "Save Visit"**
5. **Expected**: Success message, visit is saved

### Create Data for Tenant B

1. **Switch to "Hospital B"** (keep Doctor role)
2. **Go to Visit page**
3. **Fill out the form**:
   - Patient ID: `PATIENT_B_001`
   - Name: `Jane Smith`
   - Age: `28`
   - Height: `165`
   - Weight: `60`
   - HbA1c: `9.2`
4. **Click "Save Visit"**
5. **Expected**: Success message, visit is saved

### Verify Data Isolation

1. **Go to Visit History page** (while on Hospital B)
2. **Expected**: You should only see Jane Smith's visit
3. **Switch back to Hospital A**
4. **Go to Visit History page**
5. **Expected**: You should only see John Doe's visit

## Step 4: Test RBAC (Role-Based Access Control)

### Test Doctor Role

1. **Set tenant to "Hospital A"** and role to "Doctor"
2. **Go to Visit page**
3. **Expected**: You should see all fields including HbA1c
4. **Go to Configurator page**
5. **Expected**: You should see all form fields and can edit them

### Test Nurse Role

1. **Switch role to "Nurse"** (keep Hospital A)
2. **Go to Visit page**
3. **Expected**: You should see most fields but HbA1c might be restricted
4. **Go to Configurator page**
5. **Expected**: Limited access to form configuration

### Test Clerk Role

1. **Switch role to "Clerk"** (keep Hospital A)
2. **Go to Visit page**
3. **Expected**: You should see only basic fields (name, age, patient ID)
4. **Go to Configurator page**
5. **Expected**: Very limited access

## Step 5: Test Workflow Execution

### Test Diabetes Educator Workflow

1. **Set tenant to "Hospital A"** and role to "Doctor"
2. **Go to Visit page**
3. **Fill out the form** with HbA1c >= 9:
   - Patient ID: `PATIENT_A_002`
   - Name: `High HbA1c Patient`
   - Age: `45`
   - Height: `180`
   - Weight: `90`
   - HbA1c: `9.5`
4. **Click "Save Visit"**
5. **Go to Tasks page**
6. **Expected**: You should see a diabetes educator task
7. **Go to Notifications page**
8. **Expected**: You should see a notification about booking educator session

### Test Pediatrics Workflow

1. **Fill out the form** with age < 18:
   - Patient ID: `PATIENT_A_003`
   - Name: `Minor Patient`
   - Age: `12`
   - Height: `150`
   - Weight: `45`
   - HbA1c: `7.5`
2. **Expected**: Guardian fields should appear automatically
3. **Fill in Guardian Name**: `Parent Name`
4. **Click "Save Visit"**
5. **Go to Tasks page**
6. **Expected**: You should see a birth certificate upload task

## Step 6: Test Rate Limiting

### Test Submission Rate Limiting

1. **Set tenant to "Hospital A"** and role to "Doctor"
2. **Go to Visit page**
3. **Rapidly submit multiple visits** (try 10-15 times quickly)
4. **Expected**: After a certain number of submissions, you should get a rate limit error
5. **Wait a minute** and try again
6. **Expected**: Rate limit should reset

## Step 7: Test Cross-Tenant Security

### Verify Complete Isolation

1. **Create data in Hospital A**:
   - Patient ID: `SECRET_PATIENT`
   - Name: `Confidential Patient`
   - Age: `50`
   - Height: `170`
   - Weight: `75`
   - HbA1c: `8.0`

2. **Switch to Hospital B**
3. **Go to Visit History**
4. **Expected**: You should NOT see the confidential patient
5. **Try to access the patient directly** (if possible)
6. **Expected**: Access should be denied

## Step 8: Test Error Handling

### Test Missing Tenant Context

1. **Open browser developer tools** (F12)
2. **Go to Network tab**
3. **Clear the tenant from localStorage**:
   ```javascript
   localStorage.removeItem('current_tenant')
   ```
4. **Refresh the page**
5. **Try to access any page**
6. **Expected**: You should get a 401 error or be redirected to set tenant

### Test Invalid Tenant

1. **Set an invalid tenant** in the switcher
2. **Try to access data**
3. **Expected**: You should get appropriate error messages

## Step 9: Test Performance

### Test Large Data Sets

1. **Create multiple patients** for different tenants
2. **Switch between tenants** rapidly
3. **Expected**: Data should load quickly and correctly
4. **Check browser console** for any errors

## Step 10: Test UI Components

### Test Tenant Switcher

1. **Click the Tenant Switcher**
2. **Verify all options** are available
3. **Test switching** between different combinations
4. **Verify the UI updates** correctly

### Test Form Validation

1. **Test required field validation** with different roles
2. **Test field visibility** based on age (pediatrics workflow)
3. **Test file upload** functionality (if available)

## Troubleshooting

### Common Issues

1. **"Tenant context required" error**:
   - Make sure the Tenant Switcher is set
   - Check browser console for errors
   - Refresh the page

2. **Empty data in lists**:
   - Verify you're on the correct tenant
   - Check if data was created for that tenant
   - Look for error messages in console

3. **Rate limiting issues**:
   - Wait for the rate limit to reset
   - Check if you're making too many requests
   - Try with a different tenant

4. **RBAC not working**:
   - Verify the role is set correctly
   - Check if policies exist for the tenant
   - Try with a different role

### Debug Commands

Open browser console and run:

```javascript
// Check current tenant context
console.log('Tenant:', localStorage.getItem('current_tenant'))
console.log('Roles:', localStorage.getItem('current_roles'))
console.log('Departments:', localStorage.getItem('current_departments'))

// Set tenant context manually
localStorage.setItem('current_tenant', 'TENANT_A')
localStorage.setItem('current_roles', 'Doctor')
localStorage.setItem('current_departments', 'Endocrinology')
location.reload()
```

## Expected Results

After completing all tests, you should verify:

- ✅ **Complete data isolation** between tenants
- ✅ **Role-based access control** working correctly
- ✅ **Workflow execution** per tenant
- ✅ **Rate limiting** preventing abuse
- ✅ **UI components** working properly
- ✅ **Error handling** for invalid states
- ✅ **Performance** acceptable for all operations

## Conclusion

The multi-tenancy system provides complete tenant isolation with robust security and performance features. Use this guide to thoroughly test all aspects of the system and ensure it meets your requirements.

If you encounter any issues, check the browser console for error messages and refer to the troubleshooting section above.
