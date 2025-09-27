import React, { useState, useEffect } from 'react'
import { getCurrentTenant, getCurrentRoles, getCurrentDepartments, setTenantContext } from '../lib/api'

export default function TenantSwitcher({ onRoleChange }) {
  const [tenant, setTenant] = useState(getCurrentTenant())
  const [role, setRole] = useState(getCurrentRoles())
  const [department, setDepartment] = useState(getCurrentDepartments())
  const [isOpen, setIsOpen] = useState(false)

  useEffect(() => {
    setTenant(getCurrentTenant())
    setRole(getCurrentRoles())
    setDepartment(getCurrentDepartments())
  }, [])

  const handleTenantChange = (newTenant) => {
    setTenant(newTenant)
    setTenantContext(newTenant, role, department)
    if (onRoleChange) onRoleChange()
  }

  const handleRoleChange = (newRole) => {
    setRole(newRole)
    setTenantContext(tenant, newRole, department)
    if (onRoleChange) onRoleChange()
  }

  const handleDepartmentChange = (newDepartment) => {
    setDepartment(newDepartment)
    setTenantContext(tenant, role, newDepartment)
    if (onRoleChange) onRoleChange()
  }

  return (
    <div className="tenant-switcher">
      <button 
        className="btn btn-secondary btn-sm"
        onClick={() => setIsOpen(!isOpen)}
      >
        🏢 {tenant} | {role} | {department}
      </button>
      
      {isOpen && (
        <div className="tenant-dropdown">
          <div className="form-group">
            <label>Tenant:</label>
            <select 
              value={tenant} 
              onChange={(e) => handleTenantChange(e.target.value)}
              className="form-select"
            >
              <option value="TENANT_A">TENANT_A</option>
              <option value="TENANT_B">TENANT_B</option>
              <option value="test-tenant">test-tenant</option>
            </select>
          </div>
          
          <div className="form-group">
            <label>Role:</label>
            <select 
              value={role} 
              onChange={(e) => handleRoleChange(e.target.value)}
              className="form-select"
            >
              <option value="Doctor">Doctor</option>
              <option value="Nurse">Nurse</option>
              <option value="Admin">Admin</option>
            </select>
          </div>
          
          <div className="form-group">
            <label>Department:</label>
            <select 
              value={department} 
              onChange={(e) => handleDepartmentChange(e.target.value)}
              className="form-select"
            >
              <option value="Endocrinology">Endocrinology</option>
              <option value="Cardiology">Cardiology</option>
              <option value="Pediatrics">Pediatrics</option>
            </select>
          </div>
        </div>
      )}
    </div>
  )
}
