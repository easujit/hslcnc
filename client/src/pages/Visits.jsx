import React, { useEffect, useState } from 'react'
import { getJSON } from '../api'

export default function Visits(){
  const [rows, setRows] = useState([])
  const [err, setErr] = useState('')

  async function load(){
    try{
      const data = await getJSON('/api/clinical/visits/')
      setRows(data)
    }catch(e){ setErr(e.message) }
  }
  useEffect(()=>{ load() }, [])

  return (
    <div className="card">
      <h2>Visit History</h2>
      <div><button onClick={load}>Refresh</button> <span className="small error">{err}</span></div>
      <table className="table">
        <thead><tr><th>Visit ID</th><th>Patient</th><th>Created</th><th>Height</th><th>Weight</th><th>BMI</th><th>HbA1c</th><th>Educator?</th></tr></thead>
        <tbody>
          {rows.map(v => (
            <tr key={v.id}>
              <td>{v.id}</td><td>{v.patient}</td><td>{v.created_at}</td>
              <td>{v.custom_data?.height_cm ?? ''}</td>
              <td>{v.custom_data?.weight_kg ?? ''}</td>
              <td>{v.custom_data?.bmi ?? ''}</td>
              <td>{v.custom_data?.hba1c ?? ''}</td>
              <td>{v.custom_data?.book_educator ? 'Yes' : ''}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
