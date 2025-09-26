import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { setTenantContext } from '../lib/api'

export default function Login() {
  const [credentials, setCredentials] = useState({
    email: '',
    password: '',
    tenant: 'TENANT_A',
    role: 'Doctor',
    department: 'Endocrinology'
  })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      // For demo purposes, accept any non-empty credentials
      if (!credentials.email || !credentials.password) {
        setError('Please enter both email and password')
        setLoading(false)
        return
      }

      // Set tenant context
      setTenantContext(credentials.tenant, credentials.role, credentials.department)
      
      // Simulate login delay
      await new Promise(resolve => setTimeout(resolve, 500))
      
      // Navigate to dashboard
      navigate('/')
    } catch (err) {
      setError('Login failed. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setCredentials(prev => ({
      ...prev,
      [name]: value
    }))
  }

  return (
    <div className="login-container">
      <div className="login-card">
        <h2 className="login-title">Hospital POC Login</h2>
        
        <form onSubmit={handleSubmit} className="login-form">
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={credentials.email}
              onChange={handleInputChange}
              required
              className="form-input"
              placeholder="Enter your email"
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={credentials.password}
              onChange={handleInputChange}
              required
              className="form-input"
              placeholder="Enter your password"
            />
          </div>

          <div className="form-group">
            <label htmlFor="tenant">Hospital/Tenant</label>
            <select
              id="tenant"
              name="tenant"
              value={credentials.tenant}
              onChange={handleInputChange}
              className="form-select"
            >
              <option value="TENANT_A">Hospital A</option>
              <option value="TENANT_B">Hospital B</option>
              <option value="TENANT_C">Clinic C</option>
              <option value="DEV">Development</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="role">Role</label>
            <select
              id="role"
              name="role"
              value={credentials.role}
              onChange={handleInputChange}
              className="form-select"
            >
              <option value="Doctor">Doctor</option>
              <option value="Nurse">Nurse</option>
              <option value="Clerk">Clerk</option>
              <option value="Admin">Admin</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="department">Department</label>
            <select
              id="department"
              name="department"
              value={credentials.department}
              onChange={handleInputChange}
              className="form-select"
            >
              <option value="Endocrinology">Endocrinology</option>
              <option value="Cardiology">Cardiology</option>
              <option value="General">General</option>
            </select>
          </div>

          {error && (
            <div className="error-message">
              {error}
            </div>
          )}

          <button 
            type="submit" 
            className="login-button"
            disabled={loading}
          >
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </form>

        <div className="login-footer">
          <p className="demo-note">
            <strong>Demo Mode:</strong> Enter any email and password to login
          </p>
        </div>
      </div>
    </div>
  )
}
