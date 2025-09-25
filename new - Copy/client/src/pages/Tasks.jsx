import React, { useEffect, useState } from 'react'
import { api } from '../lib/api'

export default function Tasks(){
  const [rows, setRows] = useState([])
  useEffect(()=>{ load() }, [])
  async function load(){ setRows(await api('/orchestrator/tasks/')) }
  async function processNow(){ await api('/orchestrator/process-now/', { method:'POST' }); await load() }
  return (
    <div>
      <h3>Tasks</h3>
      <button onClick={processNow}>Process Events Now</button>
      <table width="100%" border="1" cellPadding="6" style={{borderCollapse:'collapse', marginTop:12}}>
        <thead><tr><th>ID</th><th>Summary</th><th>Due</th><th>Status</th><th>Created</th></tr></thead>
        <tbody>
        {rows.map(r => (
          <tr key={r.id}><td>{r.id}</td><td>{r.summary}</td><td>{new Date(r.due_at).toLocaleString()}</td><td>{r.status}</td><td>{new Date(r.created_at).toLocaleString()}</td></tr>
        ))}
        </tbody>
      </table>
    </div>
  )
}