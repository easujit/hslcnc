import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { setTenantContext } from '../lib/api'

export default function Login() {
  const [tenant, setTenant] = useState('TENANT_A')
  const [role, setRole] = useState('Doctor')
  const [department, setDepartment] = useState('Endocrinology')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleLogin = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      // Simulate API call for login
      await new Promise(resolve => setTimeout(resolve, 1000)) 
      
      setTenantContext(tenant, role, department)
      navigate('/') // Redirect to dashboard after login
    } catch (err) {
      setError('Failed to login. Please check your credentials.')
      console.error('Login error:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="login-container">
      <div className="login-card">
        <h2 className="login-title">Hospital POC Login</h2>
        <form className="login-form" onSubmit={handleLogin}>
          {error && <div className="error-message">{error}</div>}
          
          <div className="form-group">
            <label htmlFor="tenant">Tenant ID</label>
            <select 
              id="tenant" 
              className="form-select"
              value={tenant} 
              onChange={(e) => setTenant(e.target.value)}
              disabled={loading}
            >
              <option value="TENANT_A">TENANT_A</option>
              <option value="TENANT_B">TENANT_B</option>
              <option value="test-tenant">test-tenant</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="role">Role</label>
            <select 
              id="role" 
              className="form-select"
              value={role} 
              onChange={(e) => setRole(e.target.value)}
              disabled={loading}
            >
              <option value="Doctor">Doctor</option>
              <option value="Nurse">Nurse</option>
              <option value="Admin">Admin</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="department">Department</label>
            <select 
              id="department" 
              className="form-select"
              value={department} 
              onChange={(e) => setDepartment(e.target.value)}
              disabled={loading}
            >
              <option value="Endocrinology">Endocrinology</option>
              <option value="Cardiology">Cardiology</option>
              <option value="Pediatrics">Pediatrics</option>
            </select>
          </div>
          
          <button type="submit" className="login-button" disabled={loading}>
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </form>
        <div className="login-footer">
          <p className="demo-note">
            This is a demo login. Select tenant, role, and department to proceed.
          </p>
        </div>
      </div>
    </div>
  )
}
