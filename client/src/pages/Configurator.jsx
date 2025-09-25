import React, { useEffect, useState } from 'react'
import { getJSON, postJSON } from '../api'

const formName = 'visit_opd'

export default function Configurator(){
  // form
  const [formJson, setFormJson] = useState('')
  const [fId, setFId] = useState('')
  const [fLabel, setFLabel] = useState('')
  const [fType, setFType] = useState('number')
  const [fRequired, setFRequired] = useState(false)

  // rules
  const [rulesJson, setRulesJson] = useState('')
  const [rWhen, setRWhen] = useState('hba1c is not None and hba1c >= 9')
  const [rAction, setRAction] = useState('set_field')
  const [rParams, setRParams] = useState({ id: '', expr: '' })

  // workflow
  const [workflowJson, setWorkflowJson] = useState('')

  async function loadForm(){
    const data = await getJSON(`/api/config/effective/form/${formName}/`)
    setFormJson(JSON.stringify(data.spec, null, 2))
  }
  function addField(){
    const obj = formJson ? JSON.parse(formJson) : {kind:'form', name:formName, fields:[]}
    obj.fields = obj.fields || []
    obj.fields.push({ id: fId, label: fLabel, type: fType, required: !!fRequired })
    setFormJson(JSON.stringify(obj, null, 2))
  }
  async function publishForm(){
    const res = await postJSON(`/api/config/publish/form/${formName}/`, JSON.parse(formJson || '{}'))
    alert('Form published v' + res.version)
  }

  async function loadRules(){
    const data = await getJSON(`/api/config/effective/rules/${formName}/`)
    setRulesJson(JSON.stringify(data.spec, null, 2))
  }
  function addRule(){
    const obj = rulesJson ? JSON.parse(rulesJson) : {kind:'rule', name: `${formName}_rules`, rules:[]}
    const when = rWhen
    let action = null
    if (rAction === 'set_field') action = { set_field: { id: rParams.id, expr: rParams.expr } }
    else if (rAction === 'set_visibility') action = { set_visibility: { id: rParams.id, visible: rParams.visible === 'true' } }
    else action = { banner: { level:'warning', text: rParams.text || 'Notice' } }
    obj.rules.push({ when, then: [action] })
    setRulesJson(JSON.stringify(obj, null, 2))
  }
  async function publishRules(){
    const res = await postJSON(`/api/config/publish/rules/${formName}/`, JSON.parse(rulesJson || '{}'))
    alert('Rules published v' + res.version)
  }

  async function loadWorkflow(){
    const data = await getJSON(`/api/config/effective/workflow/high_hba1c_followup/`)
    setWorkflowJson(JSON.stringify(data.spec, null, 2))
  }
  async function publishWorkflow(){
    let spec = {}
    try { spec = JSON.parse(workflowJson) }
    catch {
      spec = {
        kind: 'workflow',
        name: 'high_hba1c_followup',
        trigger: { on: 'submit', form: formName },
        if: 'hba1c is not None and hba1c >= 9',
        do: [
          { notify: { channel: 'endocrinology_on_call', message: 'High HbA1c ({{hba1c}}%) for patient {{patient_id}}' } },
          { create_task: { team:'diabetes_education', summary:'Schedule educator session', details:'HbA1c={{hba1c}}', due_in_days:7 } }
        ]
      }
    }
    const res = await postJSON(`/api/config/publish/workflow/high_hba1c_followup/`, spec)
    alert('Workflow published v' + res.version)
  }

  return (
    <div className="grid">
      <div className="card">
        <h2>Form Builder: {formName}</h2>
        <div className="row">
          <div className="col">
            <label>Field ID <input value={fId} onChange={e=>setFId(e.target.value)} /></label>
            <label>Label <input value={fLabel} onChange={e=>setFLabel(e.target.value)} /></label>
            <label>Type
              <select value={fType} onChange={e=>setFType(e.target.value)}>
                <option>number</option><option>text</option><option>boolean</option>
              </select>
            </label>
            <label><input type="checkbox" checked={fRequired} onChange={e=>setFRequired(e.target.checked)} /> Required</label>
            <div><button onClick={addField}>Add Field</button> <button onClick={loadForm}>Load</button> <button onClick={publishForm}>Publish</button></div>
          </div>
          <div className="col"><textarea rows="18" value={formJson} onChange={e=>setFormJson(e.target.value)} spellCheck="false"/></div>
        </div>
      </div>

      <div className="card">
        <h2>Rules Builder</h2>
        <div className="row">
          <div className="col">
            <label>When (Python expr)
              <input value={rWhen} onChange={e=>setRWhen(e.target.value)} placeholder="hba1c is not None and hba1c >= 9" />
            </label>
            <label>Action
              <select value={rAction} onChange={e=>setRAction(e.target.value)}>
                <option value="set_field">set_field</option>
                <option value="set_visibility">set_visibility</option>
                <option value="banner">banner</option>
              </select>
            </label>
            {rAction === 'set_field' && (
              <div>
                <label>Field ID <input onChange={e=>setRParams(p=>({...p, id:e.target.value}))}/></label>
                <label>Expr <input onChange={e=>setRParams(p=>({...p, expr:e.target.value}))} placeholder="round(weight_kg / ((height_cm/100)**2), 1)"/></label>
              </div>
            )}
            {rAction === 'set_visibility' && (
              <div>
                <label>Field ID <input onChange={e=>setRParams(p=>({...p, id:e.target.value}))}/></label>
                <label>Visible
                  <select onChange={e=>setRParams(p=>({...p, visible:e.target.value}))}>
                    <option>true</option><option>false</option>
                  </select>
                </label>
              </div>
            )}
            {rAction === 'banner' && (
              <div>
                <label>Text <input onChange={e=>setRParams(p=>({...p, text:e.target.value}))} placeholder="High HbA1c — consider educator session"/></label>
              </div>
            )}
            <div><button onClick={addRule}>Add Rule</button> <button onClick={loadRules}>Load</button> <button onClick={publishRules}>Publish</button></div>
          </div>
          <div className="col"><textarea rows="18" value={rulesJson} onChange={e=>setRulesJson(e.target.value)} spellCheck="false"/></div>
        </div>
      </div>

      <div className="card">
        <h2>Workflow Builder</h2>
        <div className="row">
          <div className="col">
            <div><button onClick={loadWorkflow}>Load</button> <button onClick={publishWorkflow}>Publish</button></div>
          </div>
          <div className="col"><textarea rows="12" value={workflowJson} onChange={e=>setWorkflowJson(e.target.value)} spellCheck="false"/></div>
        </div>
      </div>
    </div>
  )
}
