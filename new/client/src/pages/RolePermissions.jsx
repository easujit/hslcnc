import React, { useState, useEffect } from 'react'
import api from '../lib/api'

export default function RolePermissions() {
  const [roles, setRoles] = useState({})
  const [selectedRole, setSelectedRole] = useState(null)
  const [permissions, setPermissions] = useState([])
  const [originalPermissions, setOriginalPermissions] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [editing, setEditing] = useState(false)
  const [saving, setSaving] = useState(false)
  const [showAddModal, setShowAddModal] = useState(false)
  const [metadata, setMetadata] = useState({ resource_types: [], actions: [], resources: [] })
  const [newPermission, setNewPermission] = useState({
    resource_type: 'field',
    action: 'read',
    resource: '',
    condition: '',
    description: ''
  })

  useEffect(() => {
    loadRoles()
    loadMetadata()
  }, [])

  const loadRoles = async () => {
    try {
      setLoading(true)
      const data = await api('/policies/roles/')
      setRoles(data)
      
      // Select first role by default
      const firstRole = Object.keys(data)[0]
      if (firstRole) {
        setSelectedRole(firstRole)
        setPermissions(data[firstRole].permissions)
        setOriginalPermissions(data[firstRole].permissions)
      }
    } catch (err) {
      setError('Failed to load roles: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  const loadMetadata = async () => {
    try {
      const data = await api('/policies/metadata/')
      setMetadata(data)
    } catch (err) {
      console.error('Failed to load metadata:', err)
    }
  }

  const handleRoleSelect = (roleName) => {
    setSelectedRole(roleName)
    setPermissions(roles[roleName].permissions)
    setOriginalPermissions(roles[roleName].permissions)
    setEditing(false)
  }

  const handlePermissionChange = (permissionIndex, field, value) => {
    if (!editing) return
    
    setPermissions(prev => {
      const newPermissions = [...prev]
      newPermissions[permissionIndex] = {
        ...newPermissions[permissionIndex],
        [field]: value
      }
      return newPermissions
    })
  }

  const handleRemovePermission = (permissionIndex) => {
    if (!editing) return
    
    setPermissions(prev => {
      const newPermissions = [...prev]
      newPermissions.splice(permissionIndex, 1)
      return newPermissions
    })
  }

  const handleAddPermission = () => {
    if (!editing) return
    setShowAddModal(true)
  }

  const handleSaveNewPermission = () => {
    if (!newPermission.resource.trim()) {
      alert('Please enter a resource name')
      return
    }
    
    setPermissions(prev => [...prev, { ...newPermission }])
    setNewPermission({
      resource_type: 'field',
      action: 'read',
      resource: '',
      condition: '',
      description: ''
    })
    setShowAddModal(false)
  }

  const handleSavePermissions = async () => {
    try {
      setSaving(true)
      // This would call the update API when implemented
      await api(`/policies/roles/${selectedRole}/permissions/`, {
        method: 'POST',
        body: { permissions }
      })
      setEditing(false)
      setOriginalPermissions([...permissions])
      // Reload roles to get updated data
      await loadRoles()
    } catch (err) {
      setError('Failed to save permissions: ' + err.message)
    } finally {
      setSaving(false)
    }
  }

  const handleCancelEdit = () => {
    setEditing(false)
    setPermissions([...originalPermissions])
  }

  const hasChanges = () => {
    return JSON.stringify(permissions) !== JSON.stringify(originalPermissions)
  }

  const getResourceTypeColor = (resourceType) => {
    const colors = {
      'field': '#3b82f6',
      'record': '#10b981',
      'workflow': '#f59e0b',
      'workflow_step': '#8b5cf6',
      'config': '#ef4444',
      'consent': '#06b6d4',
      'audit': '#6b7280'
    }
    return colors[resourceType] || '#6b7280'
  }

  const getActionIcon = (action) => {
    const icons = {
      'read': '👁️',
      'write': '✏️',
      'delete': '🗑️',
      'execute': '▶️',
      'publish': '📢',
      'mask': '🎭',
      'share': '🔗',
      'export': '📤',
      'import': '📥',
      'manage': '⚙️'
    }
    return icons[action] || '❓'
  }

  if (loading) {
    return (
      <div className="role-permissions">
        <div className="loading">Loading role permissions...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="role-permissions">
        <div className="error">{error}</div>
        <button onClick={loadRoles} className="btn">Retry</button>
      </div>
    )
  }

  return (
    <div className="role-permissions">
      <div className="permissions-header">
        <h1>Role Permissions Management</h1>
        <p>Manage permissions for different user roles in the system</p>
      </div>

      <div className="permissions-layout">
        <div className="roles-sidebar">
          <h3>Roles</h3>
          <div className="roles-list">
            {Object.entries(roles).map(([roleName, role]) => (
              <div
                key={roleName}
                className={`role-card ${selectedRole === roleName ? 'active' : ''}`}
                onClick={() => handleRoleSelect(roleName)}
              >
                <div className="role-header">
                  <span className="role-icon" style={{ color: role.color }}>
                    {role.icon}
                  </span>
                  <div className="role-info">
                    <h4>{role.display_name}</h4>
                    <p>{role.description}</p>
                  </div>
                </div>
                <div className="role-stats">
                  <span className="permission-count">
                    {role.permissions.length} permissions
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="permissions-main">
          {selectedRole && (
            <>
              <div className="permissions-header-main">
                <div className="role-title">
                  <span className="role-icon-large" style={{ color: roles[selectedRole].color }}>
                    {roles[selectedRole].icon}
                  </span>
                  <div>
                    <h2>{roles[selectedRole].display_name}</h2>
                    <p>{roles[selectedRole].description}</p>
                  </div>
                </div>
                <div className="permissions-actions">
                  {!editing ? (
                    <button 
                      className="btn btn-ghost"
                      onClick={() => setEditing(true)}
                    >
                      Edit Permissions
                    </button>
                  ) : (
                    <div className="edit-actions">
                      <button 
                        className="btn btn-ghost"
                        onClick={handleCancelEdit}
                      >
                        Cancel
                      </button>
                      <button 
                        className="btn"
                        onClick={handleSavePermissions}
                        disabled={saving || !hasChanges()}
                      >
                        {saving ? 'Saving...' : 'Save Changes'}
                      </button>
                    </div>
                  )}
                </div>
              </div>

              <div className="permissions-content">
                <div className="permissions-section">
                  <div className="section-header">
                    <h3>Permissions</h3>
                    {editing && (
                      <button 
                        className="btn btn-sm"
                        onClick={handleAddPermission}
                      >
                        + Add Permission
                      </button>
                    )}
                  </div>

                  <div className="permissions-list">
                    {permissions.map((permission, index) => (
                      <div 
                        key={index}
                        className={`permission-item ${editing ? 'editable' : ''}`}
                      >
                        <div className="permission-main">
                          <div className="permission-icon">
                            {getActionIcon(permission.action)}
                          </div>
                          <div className="permission-details">
                            {editing ? (
                              <div className="permission-edit-form">
                                <div className="edit-row">
                                  <div className="edit-field">
                                    <label>Resource Type:</label>
                                    <select
                                      value={permission.resource_type}
                                      onChange={(e) => handlePermissionChange(index, 'resource_type', e.target.value)}
                                      className="edit-select"
                                    >
                                      {metadata.resource_types.map(rt => (
                                        <option key={rt} value={rt}>{rt}</option>
                                      ))}
                                    </select>
                                  </div>
                                  <div className="edit-field">
                                    <label>Action:</label>
                                    <select
                                      value={permission.action}
                                      onChange={(e) => handlePermissionChange(index, 'action', e.target.value)}
                                      className="edit-select"
                                    >
                                      {metadata.actions.map(action => (
                                        <option key={action} value={action}>{action}</option>
                                      ))}
                                    </select>
                                  </div>
                                </div>
                                <div className="edit-row">
                                  <div className="edit-field">
                                    <label>Resource:</label>
                                    <input
                                      type="text"
                                      value={permission.resource}
                                      onChange={(e) => handlePermissionChange(index, 'resource', e.target.value)}
                                      className="edit-input"
                                      placeholder="e.g., visit_opd, patient, hba1c"
                                    />
                                  </div>
                                </div>
                                <div className="edit-row">
                                  <div className="edit-field">
                                    <label>Description:</label>
                                    <input
                                      type="text"
                                      value={permission.description || ''}
                                      onChange={(e) => handlePermissionChange(index, 'description', e.target.value)}
                                      className="edit-input"
                                      placeholder="Optional description"
                                    />
                                  </div>
                                </div>
                                <div className="edit-row">
                                  <div className="edit-field">
                                    <label>Condition:</label>
                                    <input
                                      type="text"
                                      value={permission.condition || ''}
                                      onChange={(e) => handlePermissionChange(index, 'condition', e.target.value)}
                                      className="edit-input"
                                      placeholder="Optional condition expression"
                                    />
                                  </div>
                                </div>
                              </div>
                            ) : (
                              <>
                                <div className="permission-title">
                                  <span 
                                    className="resource-type"
                                    style={{ 
                                      backgroundColor: getResourceTypeColor(permission.resource_type),
                                      color: 'white'
                                    }}
                                  >
                                    {permission.resource_type}
                                  </span>
                                  <span className="action">{permission.action}</span>
                                  <span className="resource">{permission.resource}</span>
                                </div>
                                {permission.description && (
                                  <div className="permission-description">
                                    {permission.description}
                                  </div>
                                )}
                                {permission.condition && (
                                  <div className="permission-condition">
                                    <strong>Condition:</strong> {permission.condition}
                                  </div>
                                )}
                              </>
                            )}
                          </div>
                        </div>
                        
                        {editing && (
                          <div className="permission-actions">
                            <button
                              className="btn-icon"
                              onClick={() => handleRemovePermission(index)}
                              title="Remove permission"
                            >
                              🗑️
                            </button>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </>
          )}
        </div>
      </div>

      {/* Add Permission Modal */}
      {showAddModal && (
        <div className="modal-overlay">
          <div className="modal">
            <div className="modal-header">
              <h3>Add New Permission</h3>
              <button 
                className="modal-close"
                onClick={() => setShowAddModal(false)}
              >
                ×
              </button>
            </div>
            <div className="modal-body">
              <div className="form-group">
                <label>Resource Type:</label>
                <select
                  value={newPermission.resource_type}
                  onChange={(e) => setNewPermission({...newPermission, resource_type: e.target.value})}
                  className="form-select"
                >
                  {metadata.resource_types.map(rt => (
                    <option key={rt} value={rt}>{rt}</option>
                  ))}
                </select>
              </div>
              
              <div className="form-group">
                <label>Action:</label>
                <select
                  value={newPermission.action}
                  onChange={(e) => setNewPermission({...newPermission, action: e.target.value})}
                  className="form-select"
                >
                  {metadata.actions.map(action => (
                    <option key={action} value={action}>{action}</option>
                  ))}
                </select>
              </div>
              
              <div className="form-group">
                <label>Resource:</label>
                <input
                  type="text"
                  value={newPermission.resource}
                  onChange={(e) => setNewPermission({...newPermission, resource: e.target.value})}
                  className="form-input"
                  placeholder="e.g., visit_opd, patient, hba1c"
                  required
                />
              </div>
              
              <div className="form-group">
                <label>Description (Optional):</label>
                <input
                  type="text"
                  value={newPermission.description}
                  onChange={(e) => setNewPermission({...newPermission, description: e.target.value})}
                  className="form-input"
                  placeholder="Description of this permission"
                />
              </div>
              
              <div className="form-group">
                <label>Condition (Optional):</label>
                <input
                  type="text"
                  value={newPermission.condition}
                  onChange={(e) => setNewPermission({...newPermission, condition: e.target.value})}
                  className="form-input"
                  placeholder="Condition expression (e.g., 'Doctor' in user.roles)"
                />
              </div>
            </div>
            <div className="modal-footer">
              <button 
                className="btn btn-ghost"
                onClick={() => setShowAddModal(false)}
              >
                Cancel
              </button>
              <button 
                className="btn"
                onClick={handleSaveNewPermission}
              >
                Add Permission
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
