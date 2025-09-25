import React from 'react'
import { Link } from 'react-router-dom'

export default function App({ children }){
  return (
    <div style={{fontFamily:'Inter, system-ui, Arial', padding:'16px'}}>
      <h2>Hospital Customizable App – POC</h2>
      <nav style={{display:'flex', gap:'12px', marginBottom:'16px'}}>
        <Link to="/">Dashboard</Link>
        <Link to="/visit">Visit</Link>
        <Link to="/config">Configurator</Link>
        <Link to="/visits">Visit History</Link>
        <Link to="/notifications">Notifications</Link>
        <Link to="/tasks">Tasks</Link>
      </nav>
      <div style={{border:'1px solid #ddd', borderRadius:12, padding:16}}>
        {children}
      </div>
    </div>
  )
}