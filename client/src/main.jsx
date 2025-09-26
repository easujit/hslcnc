import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import './styles.css'
import ErrorBoundary from './components/ErrorBoundary.jsx'
import App from './pages/App.jsx'
import Login from './pages/Login.jsx'
import Dashboard from './pages/Dashboard.jsx'
import Visit from './pages/Visit.jsx'
import Configurator from './pages/Configurator.jsx'
import VisitsList from './pages/VisitsList.jsx'
import Notifications from './pages/Notifications.jsx'
import Tasks from './pages/Tasks.jsx'
import RBACTest from './pages/RBACTest.jsx'
import ConsentManagement from './pages/ConsentManagement.jsx'
import RolePermissions from './pages/RolePermissions.jsx'
import PermissionManagement from './pages/PermissionManagement.jsx'

createRoot(document.getElementById('root')).render(
  <ErrorBoundary>
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/*" element={
          <App>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/visit" element={<Visit />} />
              <Route path="/config" element={<Configurator />} />
              <Route path="/visits" element={<VisitsList />} />
              <Route path="/consent" element={<ConsentManagement />} />
              <Route path="/notifications" element={<Notifications />} />
              <Route path="/tasks" element={<Tasks />} />
              <Route path="/rbac-test" element={<RBACTest />} />
              <Route path="/role-permissions" element={<RolePermissions />} />
              <Route path="/permission-management" element={<PermissionManagement />} />
            </Routes>
          </App>
        } />
      </Routes>
    </BrowserRouter>
  </ErrorBoundary>
)