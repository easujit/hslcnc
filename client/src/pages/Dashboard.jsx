import React, { useState, useEffect } from 'react'
import api from '../lib/api'

export default function Dashboard() {
  const [stats, setStats] = useState({
    patients: 0,
    visits: 0,
    consents: 0,
    tasks: 0
  })
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchStats()
  }, [])

  const fetchStats = async () => {
    try {
      const [patients, visits, consents] = await Promise.all([
        api('/clinical/patients/').catch(() => []),
        api('/clinical/visits/').catch(() => []),
        api('/consent/consents/').catch(() => [])
      ])

      setStats({
        patients: patients.length,
        visits: visits.length,
        consents: consents.length,
        tasks: 0 // Placeholder
      })
    } catch (error) {
      console.error('Failed to fetch stats:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner">⏳</div>
        <p>Loading dashboard...</p>
      </div>
    )
  }

  return (
    <div>
      <div className="card">
        <h3 className="card-title">Dashboard</h3>
        <p>Welcome to the Hospital POC system. Here's an overview of your data:</p>
        
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginTop: '1.5rem' }}>
          <div className="stat-card">
            <h4>👥 Patients</h4>
            <div className="stat-number">{stats.patients}</div>
          </div>
          <div className="stat-card">
            <h4>🏥 Visits</h4>
            <div className="stat-number">{stats.visits}</div>
          </div>
          <div className="stat-card">
            <h4>🔐 Consents</h4>
            <div className="stat-number">{stats.consents}</div>
          </div>
          <div className="stat-card">
            <h4>✅ Tasks</h4>
            <div className="stat-number">{stats.tasks}</div>
          </div>
        </div>
      </div>

      <div className="card">
        <h3 className="card-title">Quick Actions</h3>
        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <button className="btn btn-primary">New Patient</button>
          <button className="btn btn-primary">New Visit</button>
          <button className="btn btn-secondary">View Reports</button>
          <button className="btn btn-secondary">Manage Consents</button>
        </div>
      </div>
    </div>
  )
}
