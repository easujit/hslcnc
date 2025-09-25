import React, { useState } from 'react'
import { postJSON } from '../api'

export default function Dashboard(){
  const [msg, setMsg] = useState('')

  async function seed(){
    setMsg('Seeding...')
    try{
      await postJSON('/api/config/seed/', {})
      setMsg('Seeded form, rules, workflow. You can use Visit & Process Events now.')
    }catch(e){
      setMsg('Seed failed: ' + e.message)
    }
  }

  return (
    <div className="grid">
      <div className="card">
        <h2>Quick Start</h2>
        <ol>
          <li>Click <b>Seed Demo Data</b> (below).</li>
          <li>Open <b>Visit</b>, enter height/weight/HbA1c (e.g., 170/78/9.4), then <b>Save Visit</b>.</li>
          <li>Open <b>Notifications</b> or <b>Tasks</b>, click <b>Process Events Now</b>, then refresh.</li>
        </ol>
        <button onClick={seed}>Seed Demo Data</button>
        <div className={msg.includes('failed') ? 'error' : 'success'}>{msg}</div>
      </div>
    </div>
  )
}
