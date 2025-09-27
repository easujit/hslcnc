import React, { useState, useEffect } from 'react'
import { setTenantContext, getCurrentTenant, getCurrentRoles, getCurrentDepartments } from '../lib/api'

export default function TenantSwitcher({ onRoleChange }) {
  const [tenant, setTenant] = useState(getCurrentTenant())
  const [roles, setRoles] = useState(getCurrentRoles())
  const [departments, setDepartments] = useState(getCurrentDepartments())
  const [isOpen, setIsOpen] = useState(false)

  useEffect(() => {
    // Update state when localStorage changes
    setTenant(getCurrentTenant())
    setRoles(getCurrentRoles())
    setDepartments(getCurrentDepartments())
  }, [])

  const handleTenantChange = (newTenant) => {
    setTenantContext(newTenant, roles, departments)
    setTenant(newTenant)
    setIsOpen(false)
    // Reload page to refresh data with new tenant
    window.location.reload()
  }

  const handleRoleChange = (newRoles) => {
    setTenantContext(tenant, newRoles, departments)
    setRoles(newRoles)
    setIsOpen(false)
    // Call the onRoleChange callback if provided
    if (onRoleChange) {
      onRoleChange()
    } else {
      // Fallback to page reload if no callback provided
      window.location.reload()
    }
  }

  const tenantOptions = [
    { value: 'TENANT_A', label: 'Hospital A', color: '#3b82f6' },
    { value: 'TENANT_B', label: 'Hospital B', color: '#10b981' },
    { value: 'TENANT_C', label: 'Clinic C', color: '#f59e0b' },
    { value: 'DEV', label: 'Development', color: '#6b7280' }
  ]

  const roleOptions = [
    { value: 'Doctor', label: 'Doctor', icon: '👨‍⚕️' },
    { value: 'Nurse', label: 'Nurse', icon: '👩‍⚕️' },
    { value: 'Clerk', label: 'Clerk', icon: '👤' },
    { value: 'Admin', label: 'Admin', icon: '👨‍💼' }
  ]

  const departmentOptions = [
    { value: 'Endocrinology', label: 'Endocrinology' },
    { value: 'Cardiology', label: 'Cardiology' },
    { value: 'Pediatrics', label: 'Pediatrics' },
    { value: 'General', label: 'General Medicine' }
  ]

  const currentTenant = tenantOptions.find(t => t.value === tenant)
  const currentRole = roleOptions.find(r => r.value === roles)

  const handleSettingsClick = (e) => {
    e.stopPropagation()
    // Navigate to role permissions page
    window.location.href = '/role-permissions'
  }

  return (
    <div className="tenant-switcher">
      <button 
        className="settings-button"
        onClick={handleSettingsClick}
        title="Role Permissions Settings"
      >
        ⚙️
      </button>
      <div className="tenant-switcher-main">
        <div className="tenant-switcher-label">Environment:</div>
        <button 
          className="tenant-switcher-button"
          onClick={() => setIsOpen(!isOpen)}
        >
          <div className="tenant-info">
            <div className="tenant-badge" style={{ backgroundColor: currentTenant?.color }}>
              {currentTenant?.label}
            </div>
            <div className="role-info">
              {currentRole?.icon} {currentRole?.label}
            </div>
          </div>
          <span className="dropdown-arrow">▼</span>
        </button>
      </div>

      {isOpen && (
        <div className="tenant-dropdown">
          <div className="dropdown-section">
            <h4>Select Tenant</h4>
            {tenantOptions.map(option => (
              <button
                key={option.value}
                className={`tenant-option ${tenant === option.value ? 'active' : ''}`}
                onClick={() => handleTenantChange(option.value)}
              >
                <div 
                  className="tenant-color" 
                  style={{ backgroundColor: option.color }}
                ></div>
                {option.label}
              </button>
            ))}
          </div>

          <div className="dropdown-section">
            <h4>Select Role</h4>
            {roleOptions.map(option => (
              <button
                key={option.value}
                className={`role-option ${roles === option.value ? 'active' : ''}`}
                onClick={() => handleRoleChange(option.value)}
              >
                <span className="role-icon">{option.icon}</span>
                {option.label}
              </button>
            ))}
          </div>

          <div className="dropdown-section">
            <h4>Department</h4>
            <select 
              value={departments} 
              onChange={(e) => {
                setTenantContext(tenant, roles, e.target.value)
                setDepartments(e.target.value)
                window.location.reload()
              }}
              className="department-select"
            >
              {departmentOptions.map(option => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>

          <div className="dropdown-footer">
            <small>
              Current: {currentTenant?.label} • {currentRole?.label} • {departments}
            </small>
          </div>
        </div>
      )}
    </div>
  )
}
