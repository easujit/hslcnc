import React, { useEffect, useState } from 'react'
import { api } from '../lib/api'

export default function Visits(){
  const [rows, setRows] = useState([])
  useEffect(()=>{ load() }, [])
  async function load(){ setRows(await api('/clinical/visits/')) }
  return (
    <div className="card">
      <h3 className="card-title">Visit History</h3>
      <table className="table">
        <thead><tr><th>ID</th><th>Patient</th><th>Type</th><th>HbA1c</th><th>BMI</th><th>Created</th></tr></thead>
        <tbody>
        {rows.map(r => (
          <tr key={r.id}>
            <td>{r.id}</td>
            <td>{r.patient}</td>
            <td>{r.visit_type}</td>
            <td>{r.custom_data?.hba1c ?? '-'}</td>
            <td>{r.custom_data?.bmi ?? '-'}</td>
            <td>{new Date(r.created_at).toLocaleString()}</td>
          </tr>
        ))}
        </tbody>
      </table>
    </div>
  )
}