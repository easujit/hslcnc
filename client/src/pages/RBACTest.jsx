import React, { useState, useEffect } from 'react'
import { api } from '../lib/api'

export default function RBACTest() {
  const [userContext, setUserContext] = useState({
    tenant: 'H001',
    roles: 'Doctor',
    departments: 'Endocrinology',
    userId: 'user_001',
    username: 'test_user'
  })
  
  const [testResults, setTestResults] = useState({})
  const [loading, setLoading] = useState(false)

  const testEndpoints = [
    { name: 'Form Fields', endpoint: '/config/effective/form/visit_opd/' },
    { name: 'Visit History', endpoint: '/clinical/visits/' },
    { name: 'Notifications', endpoint: '/orchestrator/notifications/' },
    { name: 'Tasks', endpoint: '/orchestrator/tasks/' }
  ]

  async function testWithContext() {
    setLoading(true)
    const results = {}
    
    // Set headers for this test
    const headers = {
      'X-Tenant': userContext.tenant,
      'X-Roles': userContext.roles,
      'X-Departments': userContext.departments,
      'X-User-ID': userContext.userId,
      'X-Username': userContext.username
    }
    
    for (const test of testEndpoints) {
      try {
        const response = await fetch(`/api${test.endpoint}`, {
          headers: {
            'Content-Type': 'application/json',
            ...headers
          }
        })
        
        const data = await response.json()
        results[test.name] = {
          status: response.status,
          success: response.ok,
          data: data,
          error: response.ok ? null : data.error || 'Unknown error'
        }
      } catch (error) {
        results[test.name] = {
          status: 'ERROR',
          success: false,
          data: null,
          error: error.message
        }
      }
    }
    
    setTestResults(results)
    setLoading(false)
  }

  const rolePresets = [
    { name: 'Doctor (Endocrinology)', roles: 'Doctor', departments: 'Endocrinology' },
    { name: 'Nurse (Cardiology)', roles: 'Nurse', departments: 'Cardiology' },
    { name: 'Admin (All Departments)', roles: 'Admin', departments: 'Endocrinology,Cardiology' },
    { name: 'Clerk (No Special Access)', roles: 'Clerk', departments: 'General' },
    { name: 'No Role (Denied)', roles: '', departments: '' }
  ]

  function applyPreset(preset) {
    setUserContext(prev => ({
      ...prev,
      roles: preset.roles,
      departments: preset.departments
    }))
  }

  return (
    <div className="card">
      <h3 className="card-title">RBAC Testing Dashboard</h3>
      <p>Test different user roles and see how they affect access to different endpoints.</p>
      
      <div className="grid grid-2" style={{ marginBottom: '20px' }}>
        <div>
          <h4>User Context</h4>
          <div className="form-group">
            <label className="label">Tenant ID</label>
            <input 
              className="input" 
              value={userContext.tenant}
              onChange={e => setUserContext(prev => ({ ...prev, tenant: e.target.value }))}
            />
          </div>
          
          <div className="form-group">
            <label className="label">Roles (comma-separated)</label>
            <input 
              className="input" 
              value={userContext.roles}
              onChange={e => setUserContext(prev => ({ ...prev, roles: e.target.value }))}
              placeholder="Doctor, Nurse, Admin"
            />
          </div>
          
          <div className="form-group">
            <label className="label">Departments (comma-separated)</label>
            <input 
              className="input" 
              value={userContext.departments}
              onChange={e => setUserContext(prev => ({ ...prev, departments: e.target.value }))}
              placeholder="Endocrinology, Cardiology"
            />
          </div>
          
          <div className="form-group">
            <label className="label">User ID</label>
            <input 
              className="input" 
              value={userContext.userId}
              onChange={e => setUserContext(prev => ({ ...prev, userId: e.target.value }))}
            />
          </div>
          
          <div className="form-group">
            <label className="label">Username</label>
            <input 
              className="input" 
              value={userContext.username}
              onChange={e => setUserContext(prev => ({ ...prev, username: e.target.value }))}
            />
          </div>
        </div>
        
        <div>
          <h4>Role Presets</h4>
          <p className="muted-text">Click to apply common role combinations</p>
          <div className="preset-buttons">
            {rolePresets.map((preset, index) => (
              <button 
                key={index}
                className="btn btn-sm" 
                onClick={() => applyPreset(preset)}
                style={{ margin: '5px', display: 'block', width: '100%' }}
              >
                {preset.name}
              </button>
            ))}
          </div>
        </div>
      </div>
      
      <div className="form-group">
        <button 
          className="btn btn-primary" 
          onClick={testWithContext}
          disabled={loading}
        >
          {loading ? 'Testing...' : 'Test Access with Current Context'}
        </button>
      </div>
      
      {Object.keys(testResults).length > 0 && (
        <div className="test-results">
          <h4>Test Results</h4>
          <div className="results-grid">
            {Object.entries(testResults).map(([name, result]) => (
              <div key={name} className={`result-card ${result.success ? 'success' : 'error'}`}>
                <div className="result-header">
                  <h5>{name}</h5>
                  <span className={`status-badge ${result.success ? 'success' : 'error'}`}>
                    {result.success ? '✓ Allowed' : '✗ Denied'}
                  </span>
                </div>
                <div className="result-details">
                  <p><strong>Status:</strong> {result.status}</p>
                  {result.error && <p><strong>Error:</strong> {result.error}</p>}
                  {result.data && (
                    <details>
                      <summary>Response Data</summary>
                      <pre style={{ fontSize: '12px', background: '#f5f5f5', padding: '10px', borderRadius: '4px' }}>
                        {JSON.stringify(result.data, null, 2)}
                      </pre>
                    </details>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      
      <div className="rbac-info">
        <h4>How RBAC Works</h4>
        <ul>
          <li><strong>Field Access:</strong> Controls which form fields are visible/editable</li>
          <li><strong>Record Access:</strong> Controls which patient records can be viewed</li>
          <li><strong>Workflow Access:</strong> Controls which workflow steps can be executed</li>
          <li><strong>Publish Access:</strong> Controls who can publish configurations</li>
        </ul>
        <p className="muted-text">
          <strong>Note:</strong> Currently, the system operates in "development mode" - 
          if no policies exist for a tenant, all access is allowed. 
          When policies are added, RBAC enforcement will kick in.
        </p>
      </div>
    </div>
  )
}
