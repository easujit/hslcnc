import React from 'react'
import { Link } from 'react-router-dom'

export default function App({ children }){
  return (
    <div className="app-root">
      <header className="app-header">
        <h2 className="app-title">Hospital Customizable App – POC</h2>
        <nav className="app-nav">
          <Link to="/" className="nav-link">Dashboard</Link>
          <Link to="/visit" className="nav-link">Visit</Link>
          <Link to="/config" className="nav-link">Configurator</Link>
          <Link to="/visits" className="nav-link">Visit History</Link>
          <Link to="/notifications" className="nav-link">Notifications</Link>
          <Link to="/tasks" className="nav-link">Tasks</Link>
        </nav>
      </header>
      <main className="app-content">
        {children}
      </main>
    </div>
  )
}