import React, { useState } from 'react'
import { api } from '../lib/api'

export default function Dashboard(){
  const [msg, setMsg] = useState('')

  async function seed(){
    const r = await api('/config/seed/', { method:'POST' })
    setMsg(r.message || 'Seeded.')
  }

  return (
    <div className="card">
      <h3 className="card-title">Dashboard</h3>
      <p>Seed default OPD configuration and start using the app.</p>
      <button className="btn" onClick={seed}>Seed Demo Data</button>
      {msg && <p className="success-text">{msg}</p>}
      <ul className="list">
        <li>Visit page: live BMI calculation & HbA1c check</li>
        <li>Configurator: View/Publish Form, Rules, Workflow</li>
        <li>Visit History, Notifications, Tasks pages</li>
      </ul>
    </div>
  )
}