import React from 'react'
import { Routes, Route, Link, NavLink } from 'react-router-dom'
import Dashboard from './pages/Dashboard.jsx'
import Visit from './pages/Visit.jsx'
import Configurator from './pages/Configurator.jsx'
import Visits from './pages/Visits.jsx'
import Notifications from './pages/Notifications.jsx'
import Tasks from './pages/Tasks.jsx'

function Nav() {
  const link = ({isActive}) => ({ fontWeight: isActive ? '700' : '400' })
  return (
    <nav>
      <NavLink to="/" style={link}>Dashboard</NavLink>{' | '}
      <NavLink to="/visit" style={link}>Visit</NavLink>{' | '}
      <NavLink to="/configurator" style={link}>Configurator</NavLink>{' | '}
      <NavLink to="/visits" style={link}>Visit History</NavLink>{' | '}
      <NavLink to="/notifications" style={link}>Notifications</NavLink>{' | '}
      <NavLink to="/tasks" style={link}>Tasks</NavLink>
    </nav>
  )
}

export default function App(){
  return (
    <div>
      <header>
        <h1>Hospital POC (React)</h1>
        <Nav />
      </header>
      <Routes>
        <Route path="/" element={<Dashboard/>}/>
        <Route path="/visit" element={<Visit/>}/>
        <Route path="/configurator" element={<Configurator/>}/>
        <Route path="/visits" element={<Visits/>}/>
        <Route path="/notifications" element={<Notifications/>}/>
        <Route path="/tasks" element={<Tasks/>}/>
      </Routes>
    </div>
  )
}
