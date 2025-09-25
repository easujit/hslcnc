import React, { useEffect, useState } from 'react'
import { api, makeIdemKey } from '../lib/api'

export default function Visit(){
  const [form, setForm] = useState(null)
  const [data, setData] = useState({})
  const [visibility, setVisibility] = useState({})
  const [message, setMessage] = useState('')

  useEffect(()=>{
    loadForm()
  },[])

  async function loadForm(){
    const f = await api('/config/effective/form/visit_opd/')
    setForm(f)
    // Initialize visibility
    const vis = {}
    ;(f.fields || []).forEach(x => { if(x.visible !== undefined) vis[x.id] = !!x.visible })
    setVisibility(vis)
  }

  async function evaluate(changes){
    const next = {...data, ...changes}
    setData(next)
    const r = await api('/runtime/rules/evaluate/visit_opd/', { method:'POST', body: next })
    // Apply setField
    const updated = {...next}
    for(const s of (r.setField || [])){
      updated[s.id] = s.value
    }
    setData(updated)
    // Apply visibility
    const vis = {...visibility}
    for(const v of (r.visibility || [])){
      vis[v.id] = !!v.visible
    }
    setVisibility(vis)
  }

  function onChange(id, value){
    evaluate({ [id]: value === '' ? null : (isNaN(value) ? value : Number(value)) })
  }

  async function save(){
    const idem = makeIdemKey()
    const res = await api('/submit/forms/visit_opd/submit/', {
      method:'POST',
      headers:{ 'Idempotency-Key': idem },
      body: data
    })
    setMessage('Saved visit #' + res.visit_id + ' | BMI=' + res.bmi + (res.diabetes_educator_required ? ' | Educator Required' : ''))
  }

  if(!form) return <p>Loading form…</p>

  return (
    <div>
      <h3>OPD Visit</h3>
      <div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'12px'}}>
        {(form.fields || []).map(f => {
          if(visibility[f.id] === false) return null
          const common = { id:f.id, value: data[f.id] ?? '', onChange: e => onChange(f.id, e.target.value), disabled: f.readonly }
          return (
            <div key={f.id}>
              <label style={{display:'block', fontWeight:600}}>{f.label}</label>
              {f.type === 'number' && <input type="number" step="any" {...common} />}
              {f.type === 'text' && <input type="text" {...common} />}
              {f.type === 'checkbox' && <input type="checkbox" checked={!!data[f.id]} onChange={e => evaluate({[f.id]: e.target.checked})} disabled={f.readonly}/>}
              {f.type === 'note' && <div style={{padding:'8px', background:'#fff8e1', border:'1px solid #f0d88a', borderRadius:8}}>Book Diabetes Educator session</div>}
            </div>
          )
        })}
      </div>
      <div style={{marginTop:16}}>
        <button onClick={save}>Save Visit</button>
        {message && <p style={{color:'green'}}>{message}</p>}
      </div>
    </div>
  )
}