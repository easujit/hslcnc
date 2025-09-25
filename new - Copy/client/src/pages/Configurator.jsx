import React, { useEffect, useState } from 'react'
import { api } from '../lib/api'

function JsonEditor({ value, onChange, height=200 }){
  const [txt, setTxt] = useState(JSON.stringify(value, null, 2))
  useEffect(()=>{ setTxt(JSON.stringify(value, null, 2)) }, [value])
  return (
    <textarea style={{width:'100%', height, fontFamily:'monospace'}} value={txt} onChange={e=>setTxt(e.target.value)} onBlur={()=>{
      try{ onChange(JSON.parse(txt)) }catch(e){ /* ignore */ }
    }}/>
  )
}

export default function Configurator(){
  const [form, setForm] = useState({})
  const [rules, setRules] = useState({})
  const [workflow, setWorkflow] = useState({})
  const [msg, setMsg] = useState('')

  async function loadAll(){
    setForm(await api('/config/effective/form/visit_opd/'))
    setRules(await api('/config/effective/rules/visit_opd/'))
    setWorkflow(await api('/config/effective/workflow/visit_opd/'))
  }

  useEffect(()=>{ loadAll() }, [])

  async function publish(kind, spec){
    const r = await api(`/config/publish/${kind}/visit_opd/`, { method:'POST', body: spec })
    setMsg(`Published ${kind} v${r.version}`)
  }

  return (
    <div>
      <h3>Configurator</h3>
      <p>View or edit JSON below and click Publish to create a new version.</p>
      <h4>Form</h4>
      <JsonEditor value={form} onChange={setForm} height={220}/>
      <button onClick={()=>publish('form', form)}>Publish Form</button>

      <h4 style={{marginTop:16}}>Rules</h4>
      <JsonEditor value={rules} onChange={setRules} height={220}/>
      <button onClick={()=>publish('rule', rules)}>Publish Rules</button>

      <h4 style={{marginTop:16}}>Workflow</h4>
      <JsonEditor value={workflow} onChange={setWorkflow} height={140}/>
      <button onClick={()=>publish('workflow', workflow)}>Publish Workflow</button>

      {msg && <p style={{color:'green'}}>{msg}</p>}
    </div>
  )
}