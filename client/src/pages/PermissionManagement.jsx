import React, { useState, useEffect } from 'react'
import api from '../lib/api'

export default function PermissionManagement() {
  const [permissions, setPermissions] = useState({})
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [message, setMessage] = useState('')
  const [editingPolicy, setEditingPolicy] = useState(null)
  const [editForm, setEditForm] = useState({ effect: '', condition: '' })

  useEffect(() => {
    loadPermissions()
  }, [])

  const loadPermissions = async () => {
    try {
      setLoading(true)
      const response = await api('/policies/permissions/')
      setPermissions(response)
    } catch (err) {
      setError('Failed to load permissions: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleEditPolicy = (policy) => {
    setEditingPolicy(policy)
    setEditForm({
      effect: policy.effect,
      condition: policy.condition || ''
    })
  }

  const handleSavePolicy = async () => {
    try {
      await api('/policies/permissions/update/', {
        method: 'POST',
        body: {
          policy_id: editingPolicy.id,
          effect: editForm.effect,
          condition: editForm.condition
        }
      })
      
      setMessage('Permission updated successfully!')
      setEditingPolicy(null)
      setEditForm({ effect: '', condition: '' })
      loadPermissions()
      
      // Clear message after 3 seconds
      setTimeout(() => setMessage(''), 3000)
    } catch (err) {
      setError('Failed to update permission: ' + err.message)
    }
  }

  const handleDeletePolicy = async (policyId) => {
    if (!confirm('Are you sure you want to delete this permission?')) {
      return
    }

    try {
      await api(`/policies/permissions/${policyId}/delete/`, {
        method: 'DELETE'
      })
      
      setMessage('Permission deleted successfully!')
      loadPermissions()
      
      // Clear message after 3 seconds
      setTimeout(() => setMessage(''), 3000)
    } catch (err) {
      setError('Failed to delete permission: ' + err.message)
    }
  }

  const renderPolicyList = (resourceType, action, policies) => (
    <div key={`${resourceType}-${action}`} className="policy-section">
      <h3 className="policy-section-title">
        {resourceType.charAt(0).toUpperCase() + resourceType.slice(1)} - {action.charAt(0).toUpperCase() + action.slice(1)}
      </h3>
      <div className="policy-list">
        {policies.map((policy, index) => (
          <div key={index} className="policy-item">
            <div className="policy-info">
              <div className="policy-selector">
                <strong>Selector:</strong> {JSON.stringify(policy.selector)}
              </div>
              <div className="policy-details">
                <span className={`policy-effect ${policy.effect}`}>
                  {policy.effect.toUpperCase()}
                </span>
                {policy.condition && (
                  <span className="policy-condition">
                    Condition: {policy.condition}
                  </span>
                )}
                <span className="policy-version">v{policy.version}</span>
              </div>
            </div>
            <div className="policy-actions">
              <button 
                className="btn btn-sm"
                onClick={() => handleEditPolicy(policy)}
              >
                Edit
              </button>
              <button 
                className="btn btn-sm btn-danger"
                onClick={() => handleDeletePolicy(policy.id)}
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )

  if (loading) {
    return (
      <div className="page-container">
        <div className="loading-container">
          <div className="loading-spinner">⏳</div>
          <p>Loading permissions...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Permission Management</h1>
        <p>Manage role-based access control permissions for all users</p>
      </div>

      {error && (
        <div className="alert alert-error">
          {error}
        </div>
      )}

      {message && (
        <div className="alert alert-success">
          {message}
        </div>
      )}

      <div className="permissions-container">
        {Object.keys(permissions).length === 0 ? (
          <div className="empty-state">
            <p>No permissions found</p>
          </div>
        ) : (
          Object.entries(permissions).map(([resourceType, actions]) =>
            Object.entries(actions).map(([action, policies]) =>
              renderPolicyList(resourceType, action, policies)
            )
          )
        )}
      </div>

      {/* Edit Modal */}
      {editingPolicy && (
        <div className="modal-overlay">
          <div className="modal">
            <div className="modal-header">
              <h3>Edit Permission</h3>
              <button 
                className="modal-close"
                onClick={() => setEditingPolicy(null)}
              >
                ×
              </button>
            </div>
            <div className="modal-body">
              <div className="form-group">
                <label>Effect:</label>
                <select 
                  value={editForm.effect}
                  onChange={(e) => setEditForm({...editForm, effect: e.target.value})}
                >
                  <option value="allow">Allow</option>
                  <option value="deny">Deny</option>
                </select>
              </div>
              <div className="form-group">
                <label>Condition (optional):</label>
                <textarea
                  value={editForm.condition}
                  onChange={(e) => setEditForm({...editForm, condition: e.target.value})}
                  placeholder="e.g., 'Doctor' in user.roles"
                  rows={3}
                />
              </div>
            </div>
            <div className="modal-footer">
              <button 
                className="btn"
                onClick={handleSavePolicy}
              >
                Save Changes
              </button>
              <button 
                className="btn btn-ghost"
                onClick={() => setEditingPolicy(null)}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
