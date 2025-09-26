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

function FieldPalette({ onAddField }){
  const fieldTypes = [
    { type: 'text', label: 'Text Input', icon: '📝' },
    { type: 'number', label: 'Number', icon: '🔢' },
    { type: 'checkbox', label: 'Checkbox', icon: '☑️' },
    { type: 'note', label: 'Note/Alert', icon: '📋' },
    { type: 'file', label: 'File Upload', icon: '📎' }
  ]

  return (
    <div className="field-palette">
      <h4>Field Types</h4>
      <p className="muted-text">Drag to add fields</p>
      <div className="palette-items">
        {fieldTypes.map(ft => (
          <div 
            key={ft.type}
            className="palette-item"
            draggable
            onDragStart={(e) => {
              e.dataTransfer.setData('field-type', ft.type)
            }}
          >
            <span className="palette-icon">{ft.icon}</span>
            <span className="palette-label">{ft.label}</span>
          </div>
        ))}
      </div>
    </div>
  )
}

function FieldEditor({ field, index, onUpdate, onRemove }){
  const [isExpanded, setIsExpanded] = useState(false)
  
  return (
    <div className={`field-editor ${isExpanded ? 'expanded' : ''}`}>
      <div className="field-header" onClick={() => setIsExpanded(!isExpanded)}>
        <div className="field-info">
          <span className="field-icon">
            {field.type === 'text' && '📝'}
            {field.type === 'number' && '🔢'}
            {field.type === 'checkbox' && '☑️'}
            {field.type === 'note' && '📋'}
            {field.type === 'file' && '📎'}
          </span>
          <span className="field-name">{field.label || 'Untitled Field'}</span>
          <span className="field-type">({field.type})</span>
        </div>
        <div className="field-actions">
          <button 
            className="btn-icon" 
            onClick={(e) => { e.stopPropagation(); onRemove(index) }}
            title="Remove field"
          >
            🗑️
          </button>
          <span className="expand-icon">{isExpanded ? '▼' : '▶'}</span>
        </div>
      </div>
      
      {isExpanded && (
        <div className="field-details">
          <div className="grid grid-2">
            <div>
              <label className="label">Field ID</label>
              <input 
                className="input" 
                value={field.id || ''} 
                onChange={e => onUpdate({ id: e.target.value })}
                placeholder="e.g., patient_name"
              />
            </div>
            <div>
              <label className="label">Label</label>
              <input 
                className="input" 
                value={field.label || ''} 
                onChange={e => onUpdate({ label: e.target.value })}
                placeholder="e.g., Patient Name"
              />
            </div>
          </div>
          
          <div className="grid grid-2">
            <div>
              <label className="label">Type</label>
              <select 
                className="select" 
                value={field.type || 'text'} 
                onChange={e => onUpdate({ type: e.target.value })}
              >
                <option value="text">Text Input</option>
                <option value="number">Number</option>
                <option value="checkbox">Checkbox</option>
                <option value="note">Note/Alert</option>
                <option value="file">File Upload</option>
              </select>
            </div>
            <div>
              <label className="label">Properties</label>
              <div className="check-group">
                <label className="check">
                  <input 
                    type="checkbox" 
                    checked={!!field.required} 
                    onChange={e => onUpdate({ required: e.target.checked })}
                  />
                  Required
                </label>
                <label className="check">
                  <input 
                    type="checkbox" 
                    checked={!!field.readonly} 
                    onChange={e => onUpdate({ readonly: e.target.checked })}
                  />
                  Read-only
                </label>
                <label className="check">
                  <input 
                    type="checkbox" 
                    checked={field.visible !== false} 
                    onChange={e => onUpdate({ visible: e.target.checked })}
                  />
                  Visible by default
                </label>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

function FormPreview({ form, data, onChange }){
  const fields = form?.fields || []
  
  return (
    <div className="form-preview">
      <h4>Live Preview</h4>
      <div className="preview-form">
        {fields.map(field => {
          if (field.visible === false) return null
          
          const common = {
            id: field.id,
            value: data[field.id] ?? '',
            onChange: (e) => onChange(field.id, e.target.value),
            disabled: field.readonly
          }
          
          return (
            <div key={field.id} className="preview-field">
              <label className="label">
                {field.label}
                {field.required && <span className="required">*</span>}
              </label>
              {field.type === 'text' && <input className="input" type="text" {...common} />}
              {field.type === 'number' && <input className="input" type="number" step="any" {...common} />}
              {field.type === 'checkbox' && (
                <input 
                  className="checkbox" 
                  type="checkbox" 
                  checked={!!data[field.id]} 
                  onChange={e => onChange(field.id, e.target.checked)}
                  disabled={field.readonly}
                />
              )}
              {field.type === 'note' && (
                <div className="note">Book Diabetes Educator session</div>
              )}
              {field.type === 'file' && (
                <div className="file-upload">
                  <div className="file-upload-label">📎 Choose File</div>
                </div>
              )}
            </div>
          )
        })}
        {fields.length === 0 && (
          <div className="empty-preview">
            <p>No fields added yet. Drag fields from the palette to start building your form.</p>
          </div>
        )}
      </div>
    </div>
  )
}

function RuleBuilder({ rules, onUpdate }){
  const [expandedRule, setExpandedRule] = useState(null)
  
  const calculations = rules?.calculations || []
  const setFields = rules?.set_fields || []
  const visibility = rules?.visibility || []
  
  function addCalculation(){
    const newCalc = { set: '', expr: '', when: '' }
    onUpdate({ ...rules, calculations: [...calculations, newCalc] })
  }
  
  function updateCalculation(index, field, value){
    const updated = [...calculations]
    updated[index] = { ...updated[index], [field]: value }
    onUpdate({ ...rules, calculations: updated })
  }
  
  function removeCalculation(index){
    const updated = calculations.filter((_, i) => i !== index)
    onUpdate({ ...rules, calculations: updated })
  }
  
  function addSetField(){
    const newSet = { id: '', value: '' }
    onUpdate({ ...rules, set_fields: [...setFields, newSet] })
  }
  
  function updateSetField(index, field, value){
    const updated = [...setFields]
    updated[index] = { ...updated[index], [field]: value }
    onUpdate({ ...rules, set_fields: updated })
  }
  
  function removeSetField(index){
    const updated = setFields.filter((_, i) => i !== index)
    onUpdate({ ...rules, set_fields: updated })
  }
  
  function addVisibility(){
    const newVis = { id: '', when: '' }
    onUpdate({ ...rules, visibility: [...visibility, newVis] })
  }
  
  function updateVisibility(index, field, value){
    const updated = [...visibility]
    updated[index] = { ...updated[index], [field]: value }
    onUpdate({ ...rules, visibility: updated })
  }
  
  function removeVisibility(index){
    const updated = visibility.filter((_, i) => i !== index)
    onUpdate({ ...rules, visibility: updated })
  }
  
  return (
    <div className="rule-builder">
      <div className="rule-section">
        <div className="section-header">
          <h4>Calculations</h4>
          <p className="muted-text">Calculate field values based on other fields</p>
          <button className="btn btn-sm" onClick={addCalculation}>+ Add Calculation</button>
        </div>
        <div className="rule-items">
          {calculations.map((calc, index) => (
            <div key={index} className="rule-item">
              <div className="rule-header" onClick={() => setExpandedRule(expandedRule === `calc-${index}` ? null : `calc-${index}`)}>
                <span className="rule-icon">🧮</span>
                <span className="rule-title">Calculate {calc.set || 'field'}</span>
                <div className="rule-actions">
                  <button className="btn-icon" onClick={(e) => { e.stopPropagation(); removeCalculation(index) }}>🗑️</button>
                  <span className="expand-icon">{expandedRule === `calc-${index}` ? '▼' : '▶'}</span>
                </div>
              </div>
              {expandedRule === `calc-${index}` && (
                <div className="rule-details">
                  <div className="grid grid-3">
                    <div>
                      <label className="label">Set Field</label>
                      <input 
                        className="input" 
                        value={calc.set || ''} 
                        onChange={e => updateCalculation(index, 'set', e.target.value)}
                        placeholder="e.g., bmi"
                      />
                    </div>
                    <div>
                      <label className="label">Expression</label>
                      <input 
                        className="input" 
                        value={calc.expr || ''} 
                        onChange={e => updateCalculation(index, 'expr', e.target.value)}
                        placeholder="e.g., weight_kg / ((height_cm/100) ** 2)"
                      />
                    </div>
                    <div>
                      <label className="label">When (Condition)</label>
                      <input 
                        className="input" 
                        value={calc.when || ''} 
                        onChange={e => updateCalculation(index, 'when', e.target.value)}
                        placeholder="e.g., height_cm and weight_kg"
                      />
                    </div>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
      
      <div className="rule-section">
        <div className="section-header">
          <h4>Set Fields</h4>
          <p className="muted-text">Set field values based on conditions</p>
          <button className="btn btn-sm" onClick={addSetField}>+ Add Set Field</button>
        </div>
        <div className="rule-items">
          {setFields.map((set, index) => (
            <div key={index} className="rule-item">
              <div className="rule-header" onClick={() => setExpandedRule(expandedRule === `set-${index}` ? null : `set-${index}`)}>
                <span className="rule-icon">⚙️</span>
                <span className="rule-title">Set {set.id || 'field'}</span>
                <div className="rule-actions">
                  <button className="btn-icon" onClick={(e) => { e.stopPropagation(); removeSetField(index) }}>🗑️</button>
                  <span className="expand-icon">{expandedRule === `set-${index}` ? '▼' : '▶'}</span>
                </div>
              </div>
              {expandedRule === `set-${index}` && (
                <div className="rule-details">
                  <div className="grid grid-2">
                    <div>
                      <label className="label">Field ID</label>
                      <input 
                        className="input" 
                        value={set.id || ''} 
                        onChange={e => updateSetField(index, 'id', e.target.value)}
                        placeholder="e.g., diabetes_educator_required"
                      />
                    </div>
                    <div>
                      <label className="label">Value/Expression</label>
                      <input 
                        className="input" 
                        value={set.value || ''} 
                        onChange={e => updateSetField(index, 'value', e.target.value)}
                        placeholder="e.g., (hba1c is not None) and (hba1c >= 9)"
                      />
                    </div>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
      
      <div className="rule-section">
        <div className="section-header">
          <h4>Visibility Rules</h4>
          <p className="muted-text">Show/hide fields based on conditions</p>
          <button className="btn btn-sm" onClick={addVisibility}>+ Add Visibility Rule</button>
        </div>
        <div className="rule-items">
          {visibility.map((vis, index) => (
            <div key={index} className="rule-item">
              <div className="rule-header" onClick={() => setExpandedRule(expandedRule === `vis-${index}` ? null : `vis-${index}`)}>
                <span className="rule-icon">👁️</span>
                <span className="rule-title">Show {vis.id || 'field'}</span>
                <div className="rule-actions">
                  <button className="btn-icon" onClick={(e) => { e.stopPropagation(); removeVisibility(index) }}>🗑️</button>
                  <span className="expand-icon">{expandedRule === `vis-${index}` ? '▼' : '▶'}</span>
                </div>
              </div>
              {expandedRule === `vis-${index}` && (
                <div className="rule-details">
                  <div className="grid grid-2">
                    <div>
                      <label className="label">Field ID</label>
                      <input 
                        className="input" 
                        value={vis.id || ''} 
                        onChange={e => updateVisibility(index, 'id', e.target.value)}
                        placeholder="e.g., diabetes_educator"
                      />
                    </div>
                    <div>
                      <label className="label">When (Condition)</label>
                      <input 
                        className="input" 
                        value={vis.when || ''} 
                        onChange={e => updateVisibility(index, 'when', e.target.value)}
                        placeholder="e.g., (hba1c is not None) and (hba1c >= 9)"
                      />
                    </div>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

function WorkflowBuilder({ workflow, onUpdate }){
  const [expandedStep, setExpandedStep] = useState(null)
  
  const postSave = workflow?.post_save || []
  
  function addPostSaveStep(){
    const newStep = { emit: '', delay: 0 }
    onUpdate({ ...workflow, post_save: [...postSave, newStep] })
  }
  
  function updatePostSaveStep(index, field, value){
    const updated = [...postSave]
    updated[index] = { ...updated[index], [field]: value }
    onUpdate({ ...workflow, post_save: updated })
  }
  
  function removePostSaveStep(index){
    const updated = postSave.filter((_, i) => i !== index)
    onUpdate({ ...workflow, post_save: updated })
  }
  
  return (
    <div className="workflow-builder">
      <div className="workflow-section">
        <div className="section-header">
          <h4>Post-Save Actions</h4>
          <p className="muted-text">Actions to perform after form submission</p>
          <button className="btn btn-sm" onClick={addPostSaveStep}>+ Add Action</button>
        </div>
        <div className="workflow-items">
          {postSave.map((step, index) => (
            <div key={index} className="workflow-item">
              <div className="workflow-header" onClick={() => setExpandedStep(expandedStep === index ? null : index)}>
                <span className="workflow-icon">⚡</span>
                <span className="workflow-title">Step {index + 1}: {step.emit || 'Action'}</span>
                <div className="workflow-actions">
                  <button className="btn-icon" onClick={(e) => { e.stopPropagation(); removePostSaveStep(index) }}>🗑️</button>
                  <span className="expand-icon">{expandedStep === index ? '▼' : '▶'}</span>
                </div>
              </div>
              {expandedStep === index && (
                <div className="workflow-details">
                  <div className="grid grid-2">
                    <div>
                      <label className="label">Event Name</label>
                      <input 
                        className="input" 
                        value={step.emit || ''} 
                        onChange={e => updatePostSaveStep(index, 'emit', e.target.value)}
                        placeholder="e.g., visit_saved"
                      />
                    </div>
                    <div>
                      <label className="label">Delay (seconds)</label>
                      <input 
                        className="input" 
                        type="number"
                        value={step.delay || 0} 
                        onChange={e => updatePostSaveStep(index, 'delay', parseInt(e.target.value) || 0)}
                        placeholder="0"
                      />
                    </div>
                  </div>
                  <div className="workflow-description">
                    <p className="muted-text">
                      This will emit the event "{step.emit || 'event_name'}" after form submission
                      {step.delay > 0 && ` with a ${step.delay} second delay`}.
                    </p>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
      
      <div className="workflow-templates">
        <h4>Common Workflow Templates</h4>
        <div className="template-grid">
          <div className="template-card" onClick={() => onUpdate({ post_save: [{ emit: 'visit_saved' }] })}>
            <span className="template-icon">🏥</span>
            <h5>Basic Visit</h5>
            <p>Emit visit_saved event</p>
          </div>
          <div className="template-card" onClick={() => onUpdate({ post_save: [{ emit: 'visit_saved' }, { emit: 'send_notification', delay: 5 }] })}>
            <span className="template-icon">📧</span>
            <h5>Visit + Notification</h5>
            <p>Save visit and send notification</p>
          </div>
          <div className="template-card" onClick={() => onUpdate({ post_save: [{ emit: 'visit_saved' }, { emit: 'create_task', delay: 10 }] })}>
            <span className="template-icon">📋</span>
            <h5>Visit + Task</h5>
            <p>Save visit and create follow-up task</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default function Configurator(){
  const [form, setForm] = useState({})
  const [rules, setRules] = useState({})
  const [workflow, setWorkflow] = useState({})
  const [msg, setMsg] = useState('')
  const [dragIndex, setDragIndex] = useState(null)
  const [activeTab, setActiveTab] = useState('form')
  const [previewData, setPreviewData] = useState({})
  const [versions, setVersions] = useState({ form: [], rules: [], workflow: [] })
  const [showVersions, setShowVersions] = useState(false)

  async function loadAll(){
    setForm(await api('/config/effective/form/visit_opd/'))
    setRules(await api('/config/effective/rules/visit_opd/'))
    setWorkflow(await api('/config/effective/workflow/visit_opd/'))
    await loadVersions()
  }

  async function loadVersions(){
    try {
      const [formVersions, ruleVersions, workflowVersions] = await Promise.all([
        api('/config/versions/form/visit_opd/').catch(() => []),
        api('/config/versions/rule/visit_opd/').catch(() => []),
        api('/config/versions/workflow/visit_opd/').catch(() => [])
      ])
      setVersions({
        form: formVersions || [],
        rules: ruleVersions || [],
        workflow: workflowVersions || []
      })
    } catch (error) {
      console.error('Failed to load versions:', error)
    }
  }

  async function rollback(kind, version){
    try {
      await api(`/config/rollback/${kind}/visit_opd/`, { 
        method: 'POST', 
        body: { version } 
      })
      setMsg(`Rolled back ${kind} to version ${version}`)
      await loadAll()
    } catch (error) {
      setMsg(`Failed to rollback: ${error.message}`)
    }
  }

  useEffect(()=>{ loadAll() }, [])

  async function publish(kind, spec){
    const r = await api(`/config/publish/${kind}/visit_opd/`, { method:'POST', body: spec })
    setMsg(`Published ${kind} v${r.version}`)
  }

  // ----- Form Builder helpers -----
  const fields = Array.isArray(form?.fields) ? form.fields : []

  function updateFormFields(nextFields){
    const next = { ...(form || {}), fields: nextFields }
    setForm(next)
  }

  function addField(type = 'text'){
    const idBase = 'field_' + Math.random().toString(36).slice(2, 6)
    const nf = { id: idBase, label: 'New Field', type, required: false }
    updateFormFields([...(fields || []), nf])
  }

  function handleDrop(e){
    e.preventDefault()
    const fieldType = e.dataTransfer.getData('field-type')
    if (fieldType) {
      addField(fieldType)
    }
  }

  function handlePreviewChange(fieldId, value){
    setPreviewData(prev => ({ ...prev, [fieldId]: value }))
  }

  function removeField(index){
    const next = [...fields]
    next.splice(index, 1)
    updateFormFields(next)
  }

  function updateField(index, patch){
    const next = [...fields]
    next[index] = { ...next[index], ...patch }
    updateFormFields(next)
  }

  function onDragStart(index){
    setDragIndex(index)
  }

  function onDragOver(e){
    e.preventDefault()
  }

  function onDrop(overIndex){
    if(dragIndex === null || dragIndex === overIndex) return
    const next = [...fields]
    const [moved] = next.splice(dragIndex, 1)
    next.splice(overIndex, 0, moved)
    setDragIndex(null)
    updateFormFields(next)
  }

  return (
    <div className="card">
      <h3 className="card-title">Configurator</h3>
      <p>Configure forms, rules, and workflows for the OPD visit system.</p>
      
      <div className="tabs">
        <button 
          className={`tab ${activeTab === 'form' ? 'active' : ''}`}
          onClick={() => setActiveTab('form')}
        >
          Form
        </button>
        <button 
          className={`tab ${activeTab === 'rules' ? 'active' : ''}`}
          onClick={() => setActiveTab('rules')}
        >
          Rules
        </button>
        <button 
          className={`tab ${activeTab === 'workflow' ? 'active' : ''}`}
          onClick={() => setActiveTab('workflow')}
        >
          Workflow
        </button>
        <button 
          className={`tab ${showVersions ? 'active' : ''}`}
          onClick={() => setShowVersions(!showVersions)}
        >
          📚 Version History
        </button>
      </div>

      {activeTab === 'form' && (
        <div className="tab-content">
          <div className="form-builder">
            <div className="builder-sidebar">
              <FieldPalette onAddField={addField} />
            </div>
            
            <div className="builder-main">
              <div className="builder-header">
                <h4>Form Fields</h4>
                <p className="muted-text">Drag fields from the palette or click to add</p>
              </div>
              
              <div 
                className="fields-container"
                onDragOver={onDragOver}
                onDrop={handleDrop}
              >
                {(fields || []).map((f, idx) => (
                  <FieldEditor
                    key={f.id || idx}
                    field={f}
                    index={idx}
                    onUpdate={(patch) => updateField(idx, patch)}
                    onRemove={removeField}
                  />
                ))}
                {(!fields || fields.length === 0) && (
                  <div className="empty-fields">
                    <p>No fields added yet. Drag fields from the palette to start building your form.</p>
                  </div>
                )}
              </div>
            </div>
            
            <div className="builder-preview">
              <FormPreview 
                form={form} 
                data={previewData} 
                onChange={handlePreviewChange}
              />
            </div>
          </div>
          
          <div className="actions">
            <button className="btn" onClick={()=>publish('form', form)}>Publish Form</button>
            <button className="btn btn-ghost" onClick={() => setActiveTab('rules')}>Edit Rules</button>
          </div>
        </div>
      )}

      {activeTab === 'rules' && (
        <div className="tab-content">
          <RuleBuilder rules={rules} onUpdate={setRules} />
          <div className="actions">
            <button className="btn" onClick={()=>publish('rule', rules)}>Publish Rules</button>
            <button className="btn btn-ghost" onClick={() => setActiveTab('workflow')}>Edit Workflow</button>
          </div>
        </div>
      )}

      {activeTab === 'workflow' && (
        <div className="tab-content">
          <WorkflowBuilder workflow={workflow} onUpdate={setWorkflow} />
          <div className="actions">
            <button className="btn" onClick={()=>publish('workflow', workflow)}>Publish Workflow</button>
            <button className="btn btn-ghost" onClick={() => setActiveTab('form')}>Edit Form</button>
          </div>
        </div>
      )}

      {showVersions && (
        <div className="tab-content">
          <div className="version-history">
            <h4>Version History & Rollback</h4>
            <p className="muted-text">View and rollback to previous versions of your configurations.</p>
            
            <div className="version-sections">
              <div className="version-section">
                <h5>📝 Form Versions</h5>
                <div className="version-list">
                  {versions.form.length === 0 ? (
                    <p className="muted-text">No form versions found</p>
                  ) : (
                    versions.form.map((version, index) => (
                      <div key={version.version} className="version-item">
                        <div className="version-info">
                          <span className="version-number">v{version.version}</span>
                          <span className="version-date">{new Date(version.created_at).toLocaleString()}</span>
                          <span className="version-status">{version.status}</span>
                        </div>
                        <div className="version-actions">
                          <button 
                            className="btn btn-sm btn-secondary"
                            onClick={() => rollback('form', version.version)}
                            disabled={version.status === 'published'}
                          >
                            {version.status === 'published' ? 'Current' : 'Rollback'}
                          </button>
                        </div>
                      </div>
                    ))
                  )}
                </div>
              </div>

              <div className="version-section">
                <h5>⚙️ Rules Versions</h5>
                <div className="version-list">
                  {versions.rules.length === 0 ? (
                    <p className="muted-text">No rules versions found</p>
                  ) : (
                    versions.rules.map((version, index) => (
                      <div key={version.version} className="version-item">
                        <div className="version-info">
                          <span className="version-number">v{version.version}</span>
                          <span className="version-date">{new Date(version.created_at).toLocaleString()}</span>
                          <span className="version-status">{version.status}</span>
                        </div>
                        <div className="version-actions">
                          <button 
                            className="btn btn-sm btn-secondary"
                            onClick={() => rollback('rule', version.version)}
                            disabled={version.status === 'published'}
                          >
                            {version.status === 'published' ? 'Current' : 'Rollback'}
                          </button>
                        </div>
                      </div>
                    ))
                  )}
                </div>
              </div>

              <div className="version-section">
                <h5>🔄 Workflow Versions</h5>
                <div className="version-list">
                  {versions.workflow.length === 0 ? (
                    <p className="muted-text">No workflow versions found</p>
                  ) : (
                    versions.workflow.map((version, index) => (
                      <div key={version.version} className="version-item">
                        <div className="version-info">
                          <span className="version-number">v{version.version}</span>
                          <span className="version-date">{new Date(version.created_at).toLocaleString()}</span>
                          <span className="version-status">{version.status}</span>
                        </div>
                        <div className="version-actions">
                          <button 
                            className="btn btn-sm btn-secondary"
                            onClick={() => rollback('workflow', version.version)}
                            disabled={version.status === 'published'}
                          >
                            {version.status === 'published' ? 'Current' : 'Rollback'}
                          </button>
                        </div>
                      </div>
                    ))
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {msg && <p className="success-text">{msg}</p>}
    </div>
  )
}