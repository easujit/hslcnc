import React, { useEffect, useState } from 'react'
import { getJSON, postJSON } from '../api'

export default function Notifications(){
  const [rows, setRows] = useState([])
  const [msg, setMsg] = useState('')

  async function load(){
    const data = await getJSON('/api/orchestrator/notifications/')
    setRows(data)
  }
  async function processNow(){
    setMsg('Processing...')
    await postJSON('/api/orchestrator/process-now/', {})
    await load()
    setMsg('Done')
  }
  useEffect(()=>{ load() }, [])

  return (
    <div className="card">
      <h2>Notifications</h2>
      <div>
        <button onClick={processNow}>Process Events Now</button>
        <button onClick={load}>Refresh</button>
        <span className="small">{msg}</span>
      </div>
      <table className="table">
        <thead><tr><th>ID</th><th>Channel</th><th>Message</th><th>Status</th><th>Created</th></tr></thead>
        <tbody>
          {rows.map(n => (
            <tr key={n.id}>
              <td>{n.id}</td><td>{n.channel}</td><td>{n.message}</td><td>{n.status}</td><td>{n.created_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
