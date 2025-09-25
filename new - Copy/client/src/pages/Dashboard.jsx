import React, { useState } from 'react'
import { api } from '../lib/api'

export default function Dashboard(){
  const [msg, setMsg] = useState('')

  async function seed(){
    const r = await api('/config/seed/', { method:'POST' })
    setMsg(r.message || 'Seeded.')
  }

  return (
    <div>
      <h3>Dashboard</h3>
      <p>Seed default OPD configuration and start using the app.</p>
      <button onClick={seed}>Seed Demo Data</button>
      {msg && <p style={{color:'green'}}>{msg}</p>}
      <ul>
        <li>Visit page: live BMI calculation & HbA1c check</li>
        <li>Configurator: View/Publish Form, Rules, Workflow</li>
        <li>Visit History, Notifications, Tasks pages</li>
      </ul>
    </div>
  )
}