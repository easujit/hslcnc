import React, { useEffect, useState } from 'react'
import { api } from '../lib/api'

export default function VisitsList() {
  const [visits, setVisits] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [filter, setFilter] = useState('all') // all, completed, pending_consent, draft
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedVisit, setSelectedVisit] = useState(null)
  const [showDetails, setShowDetails] = useState(false)
  const [editingVisit, setEditingVisit] = useState(null)
  const [showEditForm, setShowEditForm] = useState(false)
  const [editData, setEditData] = useState({})
  const [message, setMessage] = useState('')

  useEffect(() => {
    loadVisits()
  }, [])

  async function loadVisits() {
    try {
      setLoading(true)
      setError('')
      const data = await api('/clinical/visits/')
      setVisits(data)
    } catch (err) {
      setError('Failed to load visits: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  async function completeVisit(visitId) {
    try {
      await api(`/clinical/visits/${visitId}/update-status/`, {
        method: 'POST'
      })
      setMessage(`Visit #${visitId} completed successfully!`)
      loadVisits() // Reload to update status
    } catch (err) {
      setError('Failed to complete visit: ' + err.message)
    }
  }

  async function editVisit(visitId) {
    try {
      const visit = visits.find(v => v.id === visitId)
      if (!visit) {
        setError('Visit not found')
        return
      }
      
      setEditingVisit(visit)
      setEditData(visit.custom_data || {})
      setShowEditForm(true)
      setError('')
    } catch (err) {
      setError('Failed to load visit for editing: ' + err.message)
    }
  }

  async function saveEditedVisit() {
    try {
      if (!editingVisit) return
      
      // Update the visit with new data
      await api(`/clinical/visits/${editingVisit.id}/`, {
        method: 'PATCH',
        body: {
          custom_data: editData
        }
      })
      
      setMessage(`Visit #${editingVisit.id} updated successfully!`)
      setShowEditForm(false)
      setEditingVisit(null)
      setEditData({})
      loadVisits() // Reload to update data
    } catch (err) {
      setError('Failed to update visit: ' + err.message)
    }
  }

  async function completeDraftVisit(visitId) {
    if (!confirm('Are you sure you want to complete this visit? This will mark it as completed and verify consent.')) {
      return
    }

    try {
      const response = await api(`/clinical/visits/${visitId}/complete/`, {
        method: 'POST'
      })
      
      setMessage('Visit completed successfully!')
      setShowEditForm(false)
      setEditingVisit(null)
      setEditData({})
      loadVisits()
      
      // Clear message after 3 seconds
      setTimeout(() => setMessage(''), 3000)
    } catch (err) {
      setError('Failed to complete visit: ' + err.message)
    }
  }

  function handleEditFieldChange(fieldId, value) {
    setEditData(prev => ({
      ...prev,
      [fieldId]: value === '' ? null : (isNaN(value) ? value : Number(value))
    }))
  }

  function getStatusBadge(status) {
    const statusConfig = {
      completed: { text: 'Completed', class: 'status-completed', icon: '✅' },
      pending_consent: { text: 'Pending Consent', class: 'status-pending', icon: '⏳' },
      draft: { text: 'Draft', class: 'status-draft', icon: '📝' },
      cancelled: { text: 'Cancelled', class: 'status-cancelled', icon: '❌' }
    }
    
    const config = statusConfig[status] || statusConfig.draft
    return (
      <span className={`status-badge ${config.class}`}>
        {config.icon} {config.text}
      </span>
    )
  }

  function getFilteredVisits() {
    let filtered = visits

    // Filter by status
    if (filter !== 'all') {
      filtered = filtered.filter(visit => visit.status === filter)
    }

    // Filter by search term
    if (searchTerm) {
      const term = searchTerm.toLowerCase()
      filtered = filtered.filter(visit => 
        visit.patient_name?.toLowerCase().includes(term) ||
        visit.patient_external_id?.toLowerCase().includes(term) ||
        visit.id.toString().includes(term)
      )
    }

    return filtered
  }

  function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  function getVisitDetails(visit) {
    const data = visit.custom_data || {}
    return {
      bmi: data.bmi?.toFixed(1) || 'N/A',
      hba1c: data.hba1c || 'N/A',
      age: data.age || 'N/A',
      height: data.height_cm || 'N/A',
      weight: data.weight_kg || 'N/A',
      educatorRequired: data.diabetes_educator_required ? 'Yes' : 'No',
      isMinor: data.age && data.age < 18 ? 'Yes' : 'No',
      guardianName: data.guardian_name || 'N/A',
      guardianRelationship: data.guardian_relationship || 'N/A'
    }
  }

  const filteredVisits = getFilteredVisits()

  if (loading) {
    return (
      <div className="card">
        <div className="loading">Loading visits...</div>
      </div>
    )
  }

  return (
    <div className="visits-list-page">
      {/* Header */}
      <div className="page-header">
        <div>
          <h1>Visit Management</h1>
          <p>Manage and track all patient visits</p>
        </div>
        <div className="header-actions">
          <button className="btn" onClick={loadVisits}>
            🔄 Refresh
          </button>
        </div>
      </div>

      {/* Filters and Search */}
      <div className="filters-section">
        <div className="filters-row">
          <div className="search-box">
            <input
              type="text"
              placeholder="Search by patient name, ID, or visit ID..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="search-input"
            />
            <span className="search-icon">🔍</span>
          </div>
          
          <div className="filter-tabs">
            <button 
              className={`filter-tab ${filter === 'all' ? 'active' : ''}`}
              onClick={() => setFilter('all')}
            >
              All ({visits.length})
            </button>
            <button 
              className={`filter-tab ${filter === 'completed' ? 'active' : ''}`}
              onClick={() => setFilter('completed')}
            >
              Completed ({visits.filter(v => v.status === 'completed').length})
            </button>
            <button 
              className={`filter-tab ${filter === 'pending_consent' ? 'active' : ''}`}
              onClick={() => setFilter('pending_consent')}
            >
              Pending ({visits.filter(v => v.status === 'pending_consent').length})
            </button>
            <button 
              className={`filter-tab ${filter === 'draft' ? 'active' : ''}`}
              onClick={() => setFilter('draft')}
            >
              Draft ({visits.filter(v => v.status === 'draft').length})
            </button>
          </div>
        </div>
      </div>

      {/* Error Message */}
      {error && (
        <div className="alert alert-error">
          {error}
        </div>
      )}

      {/* Visits Table */}
      <div className="table-container">
        <table className="visits-table">
          <thead>
            <tr>
              <th>Visit ID</th>
              <th>Patient Name</th>
              <th>Patient ID</th>
              <th>Status</th>
              <th>Visit Type</th>
              <th>BMI</th>
              <th>HbA1c</th>
              <th>Created</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredVisits.length === 0 ? (
              <tr>
                <td colSpan="9" className="empty-state">
                  {searchTerm ? 'No visits found matching your search.' : 'No visits found.'}
                </td>
              </tr>
            ) : (
              filteredVisits.map(visit => {
                const details = getVisitDetails(visit)
                return (
                  <tr key={visit.id} className="visit-row">
                    <td>
                      <span className="visit-id">#{visit.id}</span>
                    </td>
                    <td>
                      <div className="patient-name-cell">
                        {visit.patient_name || 'Unknown'}
                      </div>
                    </td>
                    <td>
                      <div className="patient-id-cell">
                        {visit.patient_external_id || 'N/A'}
                      </div>
                    </td>
                    <td>
                      {getStatusBadge(visit.status)}
                    </td>
                    <td>
                      <span className="visit-type">{visit.visit_type}</span>
                    </td>
                    <td>
                      <span className="metric-value">{details.bmi}</span>
                    </td>
                    <td>
                      <span className="metric-value">{details.hba1c}</span>
                    </td>
                    <td>
                      <span className="date-value">{formatDate(visit.created_at)}</span>
                    </td>
                    <td>
                      <div className="action-buttons">
                        <button 
                          className="btn-icon" 
                          onClick={() => {
                            setSelectedVisit(visit)
                            setShowDetails(true)
                          }}
                          title="View Details"
                        >
                          👁️
                        </button>
                        {(visit.status === 'draft' || visit.status === 'pending_consent') && (
                          <button 
                            className="btn-icon edit-btn" 
                            onClick={() => editVisit(visit.id)}
                            title="Edit Visit"
                          >
                            ✏️
                          </button>
                        )}
                        {visit.status === 'pending_consent' && (
                          <button 
                            className="btn-icon complete-btn" 
                            onClick={() => completeVisit(visit.id)}
                            title="Complete Visit"
                          >
                            ✅
                          </button>
                        )}
                      </div>
                    </td>
                  </tr>
                )
              })
            )}
          </tbody>
        </table>
      </div>

      {/* Visit Details Modal */}
      {showDetails && selectedVisit && (
        <div className="modal-overlay" onClick={() => setShowDetails(false)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h3>Visit Details - #{selectedVisit.id}</h3>
              <button 
                className="btn-close" 
                onClick={() => setShowDetails(false)}
              >
                ×
              </button>
            </div>
            <div className="modal-body">
              <div className="visit-details">
                <div className="detail-section">
                  <h4>Patient Information</h4>
                  <div className="detail-grid">
                    <div className="detail-item">
                      <label>Name:</label>
                      <span>{selectedVisit.patient_name || 'Unknown'}</span>
                    </div>
                    <div className="detail-item">
                      <label>Patient ID:</label>
                      <span>{selectedVisit.patient_external_id || 'N/A'}</span>
                    </div>
                    <div className="detail-item">
                      <label>Age:</label>
                      <span>{getVisitDetails(selectedVisit).age}</span>
                    </div>
                  </div>
                </div>

                <div className="detail-section">
                  <h4>Visit Information</h4>
                  <div className="detail-grid">
                    <div className="detail-item">
                      <label>Status:</label>
                      <span>{getStatusBadge(selectedVisit.status)}</span>
                    </div>
                    <div className="detail-item">
                      <label>Visit Type:</label>
                      <span>{selectedVisit.visit_type}</span>
                    </div>
                    <div className="detail-item">
                      <label>Created:</label>
                      <span>{formatDate(selectedVisit.created_at)}</span>
                    </div>
                    <div className="detail-item">
                      <label>Updated:</label>
                      <span>{formatDate(selectedVisit.updated_at)}</span>
                    </div>
                  </div>
                </div>

                <div className="detail-section">
                  <h4>Medical Data</h4>
                  <div className="detail-grid">
                    <div className="detail-item">
                      <label>BMI:</label>
                      <span>{getVisitDetails(selectedVisit).bmi}</span>
                    </div>
                    <div className="detail-item">
                      <label>HbA1c:</label>
                      <span>{getVisitDetails(selectedVisit).hba1c}</span>
                    </div>
                    <div className="detail-item">
                      <label>Height (cm):</label>
                      <span>{getVisitDetails(selectedVisit).height}</span>
                    </div>
                    <div className="detail-item">
                      <label>Weight (kg):</label>
                      <span>{getVisitDetails(selectedVisit).weight}</span>
                    </div>
                    <div className="detail-item">
                      <label>Educator Required:</label>
                      <span>{getVisitDetails(selectedVisit).educatorRequired}</span>
                    </div>
                    <div className="detail-item">
                      <label>Minor Patient:</label>
                      <span>{getVisitDetails(selectedVisit).isMinor}</span>
                    </div>
                  </div>
                </div>

                {getVisitDetails(selectedVisit).isMinor === 'Yes' && (
                  <div className="detail-section">
                    <h4>Guardian Information</h4>
                    <div className="detail-grid">
                      <div className="detail-item">
                        <label>Guardian Name:</label>
                        <span>{getVisitDetails(selectedVisit).guardianName}</span>
                      </div>
                      <div className="detail-item">
                        <label>Relationship:</label>
                        <span>{getVisitDetails(selectedVisit).guardianRelationship}</span>
                      </div>
                    </div>
                  </div>
                )}

                <div className="detail-section">
                  <h4>Raw Data</h4>
                  <pre className="raw-data">
                    {JSON.stringify(selectedVisit.custom_data, null, 2)}
                  </pre>
                </div>
              </div>
            </div>
            <div className="modal-footer">
              {selectedVisit.status === 'pending_consent' && (
                <button 
                  className="btn" 
                  onClick={() => {
                    completeVisit(selectedVisit.id)
                    setShowDetails(false)
                  }}
                >
                  Complete Visit
                </button>
              )}
              <button 
                className="btn btn-ghost" 
                onClick={() => setShowDetails(false)}
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Edit Visit Modal */}
      {showEditForm && editingVisit && (
        <div className="modal-overlay" onClick={() => setShowEditForm(false)}>
          <div className="modal edit-modal" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h3>Edit Visit #{editingVisit.id}</h3>
              <button 
                className="btn-close" 
                onClick={() => setShowEditForm(false)}
              >
                ×
              </button>
            </div>
            <div className="modal-body">
              <div className="edit-form">
                <div className="form-section">
                  <h4>Patient Information</h4>
                  <div className="form-grid">
                    <div className="form-group">
                      <label>Patient Name:</label>
                      <input
                        type="text"
                        value={editData.name || ''}
                        onChange={(e) => handleEditFieldChange('name', e.target.value)}
                        className="form-input"
                        placeholder="Enter patient name"
                      />
                    </div>
                    <div className="form-group">
                      <label>Age:</label>
                      <input
                        type="number"
                        value={editData.age || ''}
                        onChange={(e) => handleEditFieldChange('age', e.target.value)}
                        className="form-input"
                        placeholder="Enter age"
                      />
                    </div>
                  </div>
                </div>

                <div className="form-section">
                  <h4>Vital Signs</h4>
                  <div className="form-grid">
                    <div className="form-group">
                      <label>Height (cm):</label>
                      <input
                        type="number"
                        value={editData.height_cm || ''}
                        onChange={(e) => handleEditFieldChange('height_cm', e.target.value)}
                        className="form-input"
                        placeholder="Enter height"
                      />
                    </div>
                    <div className="form-group">
                      <label>Weight (kg):</label>
                      <input
                        type="number"
                        value={editData.weight_kg || ''}
                        onChange={(e) => handleEditFieldChange('weight_kg', e.target.value)}
                        className="form-input"
                        placeholder="Enter weight"
                      />
                    </div>
                    <div className="form-group">
                      <label>BMI:</label>
                      <input
                        type="number"
                        value={editData.bmi || ''}
                        onChange={(e) => handleEditFieldChange('bmi', e.target.value)}
                        className="form-input"
                        placeholder="Enter BMI"
                        step="0.1"
                      />
                    </div>
                  </div>
                </div>

                <div className="form-section">
                  <h4>Lab Results</h4>
                  <div className="form-grid">
                    <div className="form-group">
                      <label>HbA1c:</label>
                      <input
                        type="number"
                        value={editData.hba1c || ''}
                        onChange={(e) => handleEditFieldChange('hba1c', e.target.value)}
                        className="form-input"
                        placeholder="Enter HbA1c"
                        step="0.1"
                      />
                    </div>
                    <div className="form-group">
                      <label>Diabetes Educator Required:</label>
                      <select
                        value={editData.diabetes_educator_required ? 'true' : 'false'}
                        onChange={(e) => handleEditFieldChange('diabetes_educator_required', e.target.value === 'true')}
                        className="form-select"
                      >
                        <option value="false">No</option>
                        <option value="true">Yes</option>
                      </select>
                    </div>
                  </div>
                </div>

                {editData.age && editData.age < 18 && (
                  <div className="form-section">
                    <h4>Guardian Information (Minor Patient)</h4>
                    <div className="form-grid">
                      <div className="form-group">
                        <label>Guardian Name:</label>
                        <input
                          type="text"
                          value={editData.guardian_name || ''}
                          onChange={(e) => handleEditFieldChange('guardian_name', e.target.value)}
                          className="form-input"
                          placeholder="Enter guardian name"
                        />
                      </div>
                      <div className="form-group">
                        <label>Relationship:</label>
                        <select
                          value={editData.guardian_relationship || ''}
                          onChange={(e) => handleEditFieldChange('guardian_relationship', e.target.value)}
                          className="form-select"
                        >
                          <option value="">Select relationship</option>
                          <option value="parent">Parent</option>
                          <option value="guardian">Guardian</option>
                          <option value="sibling">Sibling</option>
                          <option value="other">Other</option>
                        </select>
                      </div>
                    </div>
                  </div>
                )}

                {message && (
                  <div className={`message ${message.includes('success') ? 'message-success' : 'message-warning'}`}>
                    {message}
                  </div>
                )}
              </div>
            </div>
            <div className="modal-footer">
              <button 
                className="btn" 
                onClick={saveEditedVisit}
              >
                Save Changes
              </button>
              {(editingVisit?.status === 'draft' || editingVisit?.status === 'pending_consent') && (
                <button 
                  className="btn complete-btn" 
                  onClick={() => completeDraftVisit(editingVisit.id)}
                  title="Complete this visit after consent verification"
                >
                  Complete Visit
                </button>
              )}
              <button 
                className="btn btn-ghost" 
                onClick={() => setShowEditForm(false)}
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
