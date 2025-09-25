import React, { useEffect, useState } from 'react'
import { getJSON, postJSON } from '../api'

export default function Tasks(){
  const [rows, setRows] = useState([])
  const [msg, setMsg] = useState('')

  async function load(){
    const data = await getJSON('/api/orchestrator/tasks/')
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
      <h2>Tasks</h2>
      <div>
        <button onClick={processNow}>Process Events Now</button>
        <button onClick={load}>Refresh</button>
        <span className="small">{msg}</span>
      </div>
      <table className="table">
        <thead><tr><th>ID</th><th>Team</th><th>Summary</th><th>Details</th><th>Due</th><th>Status</th><th>Created</th></tr></thead>
        <tbody>
          {rows.map(t => (
            <tr key={t.id}>
              <td>{t.id}</td><td>{t.team}</td><td>{t.summary}</td><td>{t.details}</td>
              <td>{t.due_at}</td><td>{t.status}</td><td>{t.created_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
