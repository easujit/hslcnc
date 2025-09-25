import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import './styles.css'
import App from './pages/App.jsx'
import Dashboard from './pages/Dashboard.jsx'
import Visit from './pages/Visit.jsx'
import Configurator from './pages/Configurator.jsx'
import Visits from './pages/Visits.jsx'
import Notifications from './pages/Notifications.jsx'
import Tasks from './pages/Tasks.jsx'

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <App>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/visit" element={<Visit />} />
        <Route path="/config" element={<Configurator />} />
        <Route path="/visits" element={<Visits />} />
        <Route path="/notifications" element={<Notifications />} />
        <Route path="/tasks" element={<Tasks />} />
      </Routes>
    </App>
  </BrowserRouter>
)