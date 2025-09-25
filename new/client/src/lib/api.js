// Get tenant context from localStorage or default
function getTenantContext() {
  const tenant = localStorage.getItem('current_tenant') || 'TENANT_A'
  const roles = localStorage.getItem('current_roles') || 'Doctor'
  const departments = localStorage.getItem('current_departments') || 'Endocrinology'
  
  return {
    'X-Tenant': tenant,
    'X-Roles': roles,
    'X-Departments': departments
  }
}

export async function api(path, opts={}){
  const tenantHeaders = getTenantContext()
  
  // Add Idempotency-Key for POST requests
  const headers = { 
    'Content-Type': 'application/json', 
    ...tenantHeaders,
    ...(opts.headers || {}) 
  }
  
  // Add Idempotency-Key for POST requests if not already provided
  if (opts.method === 'POST' && !headers['Idempotency-Key'] && !headers['idempotency-key']) {
    headers['Idempotency-Key'] = makeIdemKey()
  }
  
  const res = await fetch('/api'+path, {
    ...opts,
    headers,
    body: opts.body ? JSON.stringify(opts.body) : undefined
  })
  if(!res.ok){
    const txt = await res.text()
    throw new Error(txt || res.statusText)
  }
  return res.json()
}

// Tenant management functions
export function setTenantContext(tenant, roles = 'Doctor', departments = 'Endocrinology') {
  localStorage.setItem('current_tenant', tenant)
  localStorage.setItem('current_roles', roles)
  localStorage.setItem('current_departments', departments)
}

export function getCurrentTenant() {
  return localStorage.getItem('current_tenant') || 'TENANT_A'
}

export function getCurrentRoles() {
  return localStorage.getItem('current_roles') || 'Doctor'
}

export function getCurrentDepartments() {
  return localStorage.getItem('current_departments') || 'Endocrinology'
}

export function makeIdemKey(){
  return 'idem-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2)
}

// Default export for backward compatibility
export default api