import React, { useEffect, useState } from 'react'
import { api, makeIdemKey } from '../lib/api'

function FileUpload({ fieldId, onFileUpload, uploadedFile }) {
  const [uploading, setUploading] = useState(false)
  const [uploadError, setUploadError] = useState('')

  async function handleFileChange(e) {
    const file = e.target.files[0]
    if (!file) return

    setUploading(true)
    setUploadError('')

    try {
      const formData = new FormData()
      formData.append('file', file)
      formData.append('document_type', 'birth_certificate')
      
      const response = await fetch('/api/clinical/documents/upload/', {
        method: 'POST',
        body: formData
      })

      if (!response.ok) {
        throw new Error('Upload failed')
      }

      const result = await response.json()
      onFileUpload(fieldId, result.document_id)
    } catch (error) {
      setUploadError('Upload failed. Please try again.')
    } finally {
      setUploading(false)
    }
  }

  return (
    <div className="file-upload">
      <input
        type="file"
        id={fieldId}
        accept=".pdf,.jpg,.jpeg,.png"
        onChange={handleFileChange}
        disabled={uploading}
        style={{ display: 'none' }}
      />
      <label htmlFor={fieldId} className="file-upload-label">
        {uploading ? 'Uploading...' : uploadedFile ? '✓ File Uploaded' : 'Choose File'}
      </label>
      {uploadError && <div className="error-text">{uploadError}</div>}
      {uploadedFile && (
        <div className="uploaded-file">
          <span>📄 Birth Certificate uploaded</span>
        </div>
      )}
    </div>
  )
}

export default function Visit(){
  const [form, setForm] = useState(null)
  const [data, setData] = useState({})
  const [visibility, setVisibility] = useState({})
  const [message, setMessage] = useState('')
  const [uploadedFiles, setUploadedFiles] = useState({})

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

  function handleFileUpload(fieldId, documentId) {
    setUploadedFiles(prev => ({ ...prev, [fieldId]: documentId }))
    // Also update the data to indicate file is uploaded
    setData(prev => ({ ...prev, [fieldId]: documentId }))
  }

  function validateForm() {
    const errors = []
    for (const field of form.fields || []) {
      if (field.required && visibility[field.id] !== false) {
        const value = data[field.id]
        if (value === undefined || value === null || value === '' || value === 0) {
          errors.push(`${field.label} is required`)
        }
      }
    }
    return errors
  }

  async function save(){
    // Frontend validation
    const validationErrors = validateForm()
    if (validationErrors.length > 0) {
      setMessage('Validation errors: ' + validationErrors.join(', '))
      return
    }

    const idem = makeIdemKey()
    try {
      const res = await api('/submit/forms/visit_opd/submit/', {
        method:'POST',
        headers:{ 'Idempotency-Key': idem },
        body: data
      })
      setMessage('Saved visit #' + res.visit_id + ' | BMI=' + res.bmi + (res.diabetes_educator_required ? ' | Educator Required' : ''))
    } catch (error) {
      console.error('Save error:', error)
      setMessage('Error: ' + (error.message || 'Failed to save visit'))
    }
  }

  if(!form) return <p className="muted-text">Loading form…</p>

  return (
    <div className="card">
      <h3 className="card-title">OPD Visit</h3>
      <div className="grid grid-2">
        {(form.fields || []).map(f => {
          if(visibility[f.id] === false) return null
          const common = { id:f.id, value: data[f.id] ?? '', onChange: e => onChange(f.id, e.target.value), disabled: f.readonly }
          return (
            <div key={f.id}>
              <label className="label">
                {f.label}
                {f.required && <span className="required-asterisk"> *</span>}
              </label>
              {f.type === 'number' && <input className="input" type="number" step="any" {...common} />}
              {f.type === 'text' && <input className="input" type="text" {...common} />}
              {f.type === 'checkbox' && <input className="checkbox" type="checkbox" checked={!!data[f.id]} onChange={e => evaluate({[f.id]: e.target.checked})} disabled={f.readonly}/>}
              {f.type === 'note' && <div className="note">Book Diabetes Educator session</div>}
              {f.type === 'file' && (
                <FileUpload 
                  fieldId={f.id} 
                  onFileUpload={handleFileUpload}
                  uploadedFile={uploadedFiles[f.id]}
                />
              )}
            </div>
          )
        })}
      </div>
      <div className="actions">
        <button className="btn" onClick={save}>Save Visit</button>
        {message && <p className="success-text">{message}</p>}
      </div>
    </div>
  )
}