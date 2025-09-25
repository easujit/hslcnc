import React, { useEffect, useState } from 'react'
import { postJSON, uuidv4 } from '../api'

export default function Visit(){
  const [patientId, setPatientId] = useState('P123')
  const [height, setHeight] = useState('')
  const [weight, setWeight] = useState('')
  const [hba1c, setHba1c] = useState('')
  const [bmi, setBmi] = useState('')
  const [showEducator, setShowEducator] = useState(false)
  const [bookEducator, setBookEducator] = useState(false)
  const [warnings, setWarnings] = useState([])
  const [status, setStatus] = useState('')

  async function evaluate(){
    const values = {
      height_cm: height ? parseFloat(height) : null,
      weight_kg: weight ? parseFloat(weight) : null,
      hba1c: hba1c ? parseFloat(hba1c) : null,
      book_educator: bookEducator
    }
    const res = await fetch(`/api/runtime/rules/evaluate/visit_opd/`, {
      method: 'POST', headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ values })
    })
    const data = await res.json()
    const sf = (data.setField || []).find(x => x.id === 'bmi')
    setBmi(sf ? (sf.value ?? '') : '')
    const vis = (data.visibility || []).find(x => x.id === 'book_educator')
    setShowEducator(vis ? !!vis.visible : false)
    setWarnings(data.warnings || [])
  }

  useEffect(() => { evaluate() }, [height, weight, hba1c, bookEducator])

  async function save(){
    setStatus('Saving...')
    const idem = uuidv4()
    const payload = {
      patient_id: patientId || 'P123',
      values: {
        height_cm: height ? parseFloat(height) : null,
        weight_kg: weight ? parseFloat(weight) : null,
        hba1c: hba1c ? parseFloat(hba1c) : null,
        book_educator: bookEducator
      }
    }
    const r = await fetch(`/api/submit/forms/visit_opd/submit/`, {
      method: 'POST',
      headers: { 'Content-Type':'application/json', 'Idempotency-Key': idem },
      body: JSON.stringify(payload)
    })
    const data = await r.json()
    if (r.ok) setStatus(`Saved visit ${data.visit_id}. ${data.warnings?.join(', ') || ''}`)
    else setStatus('Error: ' + JSON.stringify(data))
  }

  return (
    <div className="card">
      <h2>Visit OPD (Live)</h2>
      <div className="row">
        <div className="col">
          <label>Patient ID
            <input value={patientId} onChange={e=>setPatientId(e.target.value)} placeholder="P123" />
          </label>
        </div>
      </div>
      <div className="row">
        <div className="col">
          <label>Height (cm)
            <input type="number" value={height} onChange={e=>setHeight(e.target.value)} />
          </label>
        </div>
        <div className="col">
          <label>Weight (kg)
            <input type="number" value={weight} onChange={e=>setWeight(e.target.value)} />
          </label>
        </div>
        <div className="col">
          <label>HbA1c (%)
            <input type="number" step="0.1" value={hba1c} onChange={e=>setHba1c(e.target.value)} />
          </label>
        </div>
        <div className="col">
          <label>BMI
            <input type="number" value={bmi} readOnly />
          </label>
        </div>
      </div>
      {showEducator && (
        <div className="row">
          <div className="col">
            <label>
              <input type="checkbox" checked={bookEducator} onChange={e=>setBookEducator(e.target.checked)} />
              {' '}Book Diabetes Educator session
            </label>
          </div>
        </div>
      )}
      <div className="warn">{warnings.join(' | ')}</div>
      <div>
        <button onClick={save}>Save Visit</button>
        <span className="small">{status}</span>
      </div>
    </div>
  )
}
