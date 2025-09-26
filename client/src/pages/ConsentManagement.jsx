import React, { useState, useEffect } from 'react'
import { api } from '../lib/api'

export default function ConsentManagement() {
  const [consents, setConsents] = useState([])
  const [patients, setPatients] = useState([])
  const [showCreateForm, setShowCreateForm] = useState(false)
  const [newConsent, setNewConsent] = useState({
    patient_id: '',
    purpose: 'treatment',
    data_categories: [],
    date_range_start: '',
    date_range_end: '',
    expiry: '',
    notice_lang: 'en',
    consent_method: 'digital',
    consent_version: '1.0',
    legal_basis: 'consent'
  })
  const [showNewPatientForm, setShowNewPatientForm] = useState(false)
  const [newPatient, setNewPatient] = useState({
    external_id: '',
    name: '',
    age: 25,
    height_cm: 170,
    weight_kg: 70
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [success, setSuccess] = useState('')

  const dataCategories = [
    'demographics', 'vitals', 'labs', 'diagnosis', 'medications',
    'procedures', 'allergies', 'family_history', 'social_history',
    'insurance', 'billing', 'images', 'documents'
  ]

  const purposes = [
    'treatment', 'ops', 'research', 'analytics', 'marketing', 'emergency'
  ]

  useEffect(() => {
    loadConsents()
    loadPatients()
  }, [])

  const loadConsents = async () => {
    try {
      const data = await api('/consent/consents/')
      setConsents(data.results || data)
    } catch (err) {
      setError('Failed to load consents: ' + err.message)
    }
  }

  const loadPatients = async () => {
    try {
      const data = await api('/clinical/patients/')
      setPatients(data)
    } catch (err) {
      console.error('Failed to load patients:', err)
    }
  }

  const handleCreateConsent = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      // Validate required fields
      if (!newConsent.patient_id) {
        setError('Please select a patient')
        setLoading(false)
        return
      }
      
      if (newConsent.data_categories.length === 0) {
        setError('Please select at least one data category')
        setLoading(false)
        return
      }

      // Set default dates
      const now = new Date()
      const oneYearLater = new Date(now.getTime() + 365 * 24 * 60 * 60 * 1000)
      
      const consentData = {
        ...newConsent,
        tenant_id: localStorage.getItem('current_tenant') || 'test-tenant',
        date_range_start: newConsent.date_range_start || now.toISOString(),
        date_range_end: newConsent.date_range_end || oneYearLater.toISOString(),
        expiry: newConsent.expiry || oneYearLater.toISOString()
      }

      await api('/consent/consents/', {
        method: 'POST',
        body: consentData
      })

      setShowCreateForm(false)
      setSuccess('Consent created successfully!')
      setNewConsent({
        patient_id: '',
        purpose: 'treatment',
        data_categories: [],
        date_range_start: '',
        date_range_end: '',
        expiry: '',
        notice_lang: 'en',
        consent_method: 'digital',
        consent_version: '1.0',
        legal_basis: 'consent'
      })
      loadConsents()
      
      // Clear success message after 3 seconds
      setTimeout(() => setSuccess(''), 3000)
    } catch (err) {
      setError('Failed to create consent: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleRevokeConsent = async (consentId) => {
    if (!confirm('Are you sure you want to revoke this consent?')) return

    try {
      await api(`/consent/consent/${consentId}/revoke/`, {
        method: 'POST',
        body: {
          reason: 'Revoked by user',
          revoked_by: 'current_user'
        }
      })
      loadConsents()
    } catch (err) {
      setError('Failed to revoke consent: ' + err.message)
    }
  }

  const handleCheckConsent = async (patientId, purpose, dataCategories) => {
    try {
      const result = await api('/consent/consent/check/', {
        method: 'POST',
        body: {
          patient_id: patientId,
          purpose: purpose,
          data_categories: dataCategories,
          action: 'read'
        }
      })
      alert(`Consent Check Result: ${result.allow ? 'ALLOWED' : 'DENIED'}\nReason: ${result.reason}`)
    } catch (err) {
      setError('Failed to check consent: ' + err.message)
    }
  }

  const handleCreateNewPatient = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      // First create consent for the patient (this will work even if patient doesn't exist yet)
      const now = new Date()
      const oneYearLater = new Date(now.getTime() + 365 * 24 * 60 * 60 * 1000)
      
      const consentData = {
        patient_id: newPatient.external_id,
        tenant_id: localStorage.getItem('current_tenant') || 'test-tenant',
        purpose: 'treatment',
        data_categories: ['demographics', 'vitals', 'labs', 'diagnosis', 'medications', 'procedures', 'documents'],
        date_range_start: now.toISOString(),
        date_range_end: oneYearLater.toISOString(),
        expiry: oneYearLater.toISOString(),
        notice_lang: 'en',
        consent_method: 'digital',
        consent_version: '1.0',
        legal_basis: 'consent'
      }

      await api('/consent/consents/', {
        method: 'POST',
        body: consentData
      })

      // Now create the patient directly without creating a visit
      const patientData = {
        external_id: newPatient.external_id,
        name: newPatient.name,
        tenant_id: localStorage.getItem('current_tenant') || 'test-tenant',
        custom_data: {
          age: newPatient.age,
          height_cm: newPatient.height_cm,
          weight_kg: newPatient.weight_kg
        }
      }

      await api('/clinical/patients/', {
        method: 'POST',
        body: patientData
      })

      setShowNewPatientForm(false)
      setNewPatient({ external_id: '', name: '', age: 25, height_cm: 170, weight_kg: 70 })
      setSuccess(`Patient ${newPatient.external_id} created and consent added!`)
      loadConsents()
      loadPatients()
      
      // Clear success message after 3 seconds
      setTimeout(() => setSuccess(''), 3000)
    } catch (err) {
      setError('Failed to create patient and consent: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString()
  }

  const getStatusColor = (status) => {
    switch (status) {
      case 'granted': return 'green'
      case 'revoked': return 'red'
      case 'expired': return 'orange'
      case 'pending': return 'blue'
      default: return 'gray'
    }
  }

  return (
    <div className="page">
      <div className="page-header">
        <h1>Consent Management</h1>
        <div className="header-actions">
          <button 
            className="btn btn-secondary"
            onClick={() => setShowNewPatientForm(true)}
          >
            + New Patient & Consent
          </button>
          <button 
            className="btn btn-primary"
            onClick={() => setShowCreateForm(true)}
          >
            Create New Consent
          </button>
        </div>
      </div>

      {error && (
        <div className="alert alert-error">
          {error}
        </div>
      )}

      {success && (
        <div className="alert alert-success">
          {success}
        </div>
      )}

      {showNewPatientForm && (
        <div 
          className="modal-overlay"
          onClick={(e) => {
            if (e.target === e.currentTarget) {
              setShowNewPatientForm(false)
            }
          }}
        >
          <div className="modal">
            <div className="modal-header">
              <h2>Create New Patient & Consent</h2>
              <button 
                className="btn-close"
                onClick={() => setShowNewPatientForm(false)}
              >
                ×
              </button>
            </div>
            <div className="modal-body">
              <form onSubmit={handleCreateNewPatient} className="form">
                <div className="form-group">
                  <label>Patient ID *</label>
                  <input
                    type="text"
                    value={newPatient.external_id}
                    onChange={(e) => setNewPatient({...newPatient, external_id: e.target.value})}
                    required
                    className="form-input"
                    placeholder="e.g., P999"
                  />
                </div>

                <div className="form-group">
                  <label>Patient Name *</label>
                  <input
                    type="text"
                    value={newPatient.name}
                    onChange={(e) => setNewPatient({...newPatient, name: e.target.value})}
                    required
                    className="form-input"
                    placeholder="e.g., John Doe"
                  />
                </div>

                <div className="form-group">
                  <label>Age *</label>
                  <input
                    type="number"
                    value={newPatient.age}
                    onChange={(e) => setNewPatient({...newPatient, age: parseInt(e.target.value) || 25})}
                    required
                    className="form-input"
                    placeholder="25"
                    min="0"
                    max="120"
                  />
                </div>

                <div className="form-group">
                  <label>Height (cm) *</label>
                  <input
                    type="number"
                    value={newPatient.height_cm}
                    onChange={(e) => setNewPatient({...newPatient, height_cm: parseInt(e.target.value) || 170})}
                    required
                    className="form-input"
                    placeholder="170"
                    min="50"
                    max="250"
                  />
                </div>

                <div className="form-group">
                  <label>Weight (kg) *</label>
                  <input
                    type="number"
                    value={newPatient.weight_kg}
                    onChange={(e) => setNewPatient({...newPatient, weight_kg: parseInt(e.target.value) || 70})}
                    required
                    className="form-input"
                    placeholder="70"
                    min="10"
                    max="300"
                  />
                </div>

                <div className="form-group">
                  <label>Consent will be created for:</label>
                  <div className="consent-preview">
                    <p><strong>Purpose:</strong> Treatment</p>
                    <p><strong>Data Categories:</strong> Demographics, Vitals, Labs, Diagnosis, Medications, Procedures, Documents</p>
                    <p><strong>Duration:</strong> 1 year from today</p>
                  </div>
                </div>
              </form>
            </div>
            <div className="modal-footer">
              <button 
                type="button" 
                className="btn btn-ghost"
                onClick={() => setShowNewPatientForm(false)}
              >
                Cancel
              </button>
              <button 
                type="submit" 
                className="btn"
                disabled={loading}
                onClick={handleCreateNewPatient}
              >
                {loading ? 'Creating...' : 'Create Patient & Consent'}
              </button>
            </div>
          </div>
        </div>
      )}

      {showCreateForm && (
        <div 
          className="modal-overlay"
          onClick={(e) => {
            if (e.target === e.currentTarget) {
              setShowCreateForm(false)
            }
          }}
        >
          <div className="modal">
            <div className="modal-header">
              <h2>Create New Consent</h2>
              <button 
                className="btn-close"
                onClick={() => setShowCreateForm(false)}
              >
                ×
              </button>
            </div>
            <div className="modal-body">
              <form onSubmit={handleCreateConsent} className="form">
                <div className="form-group">
                  <label>Patient ID *</label>
                  <select
                    value={newConsent.patient_id}
                    onChange={(e) => setNewConsent({...newConsent, patient_id: e.target.value})}
                    required
                    className="form-select"
                  >
                    <option value="">Select Patient</option>
                    {patients.map(patient => (
                      <option key={patient.id} value={patient.external_id}>
                        {patient.external_id} - {patient.name}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="form-group">
                  <label>Purpose *</label>
                  <select
                    value={newConsent.purpose}
                    onChange={(e) => setNewConsent({...newConsent, purpose: e.target.value})}
                    required
                    className="form-select"
                  >
                    {purposes.map(purpose => (
                      <option key={purpose} value={purpose}>
                        {purpose.charAt(0).toUpperCase() + purpose.slice(1)}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="form-group">
                  <label>Data Categories *</label>
                  <div className="checkbox-actions">
                    <button
                      type="button"
                      className="btn btn-sm btn-secondary"
                      onClick={() => setNewConsent({...newConsent, data_categories: [...dataCategories]})}
                    >
                      Select All
                    </button>
                    <button
                      type="button"
                      className="btn btn-sm btn-secondary"
                      onClick={() => setNewConsent({...newConsent, data_categories: []})}
                    >
                      Clear All
                    </button>
                  </div>
                  <div className="checkbox-group">
                    {dataCategories.map(category => (
                      <label key={category} className="checkbox-label">
                        <input
                          type="checkbox"
                          checked={newConsent.data_categories.includes(category)}
                          onChange={(e) => {
                            if (e.target.checked) {
                              setNewConsent({
                                ...newConsent,
                                data_categories: [...newConsent.data_categories, category]
                              })
                            } else {
                              setNewConsent({
                                ...newConsent,
                                data_categories: newConsent.data_categories.filter(c => c !== category)
                              })
                            }
                          }}
                        />
                        {category}
                      </label>
                    ))}
                  </div>
                </div>

                <div className="form-group">
                  <label>Date Range Start</label>
                  <input
                    type="datetime-local"
                    value={newConsent.date_range_start}
                    onChange={(e) => setNewConsent({...newConsent, date_range_start: e.target.value})}
                    className="form-input"
                  />
                </div>

                <div className="form-group">
                  <label>Date Range End</label>
                  <input
                    type="datetime-local"
                    value={newConsent.date_range_end}
                    onChange={(e) => setNewConsent({...newConsent, date_range_end: e.target.value})}
                    className="form-input"
                  />
                </div>

                <div className="form-group">
                  <label>Expiry</label>
                  <input
                    type="datetime-local"
                    value={newConsent.expiry}
                    onChange={(e) => setNewConsent({...newConsent, expiry: e.target.value})}
                    className="form-input"
                  />
                </div>
              </form>
            </div>
            <div className="modal-footer">
              <button 
                type="button" 
                className="btn btn-ghost"
                onClick={() => setShowCreateForm(false)}
              >
                Cancel
              </button>
              <button 
                type="submit" 
                className="btn"
                disabled={loading}
                onClick={handleCreateConsent}
              >
                {loading ? 'Creating...' : 'Create Consent'}
              </button>
            </div>
          </div>
        </div>
      )}

      <div className="consent-list">
        <h2>Existing Consents</h2>
        {consents.length === 0 ? (
          <p>No consents found.</p>
        ) : (
          <div className="table-container">
            <table className="table">
              <thead>
                <tr>
                  <th>Consent ID</th>
                  <th>Patient ID</th>
                  <th>Purpose</th>
                  <th>Data Categories</th>
                  <th>Status</th>
                  <th>Created</th>
                  <th>Expires</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {consents.map(consent => (
                  <tr key={consent.id}>
                    <td>{consent.consent_id}</td>
                    <td>{consent.patient_id}</td>
                    <td>{consent.purpose}</td>
                    <td>
                      <div className="tags">
                        {consent.data_categories.map(category => (
                          <span key={category} className="tag">
                            {category}
                          </span>
                        ))}
                      </div>
                    </td>
                    <td>
                      <span 
                        className="status-badge"
                        style={{backgroundColor: getStatusColor(consent.status)}}
                      >
                        {consent.status}
                      </span>
                    </td>
                    <td>{formatDate(consent.created_at)}</td>
                    <td>{formatDate(consent.expiry)}</td>
                    <td>
                      <div className="action-buttons">
                        <button
                          className="btn btn-sm btn-secondary"
                          onClick={() => handleCheckConsent(
                            consent.patient_id, 
                            consent.purpose, 
                            consent.data_categories
                          )}
                        >
                          Check
                        </button>
                        {consent.status === 'granted' && (
                          <button
                            className="btn btn-sm btn-danger"
                            onClick={() => handleRevokeConsent(consent.consent_id)}
                          >
                            Revoke
                          </button>
                        )}
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  )
}
