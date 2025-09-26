import React, { useState, useEffect } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import TenantSwitcher from '../components/TenantSwitcher'
import api from '../lib/api'

export default function App({ children }){
  const location = useLocation()
  const navigate = useNavigate()
  const [userPermissions, setUserPermissions] = useState(null)
  const [loading, setLoading] = useState(true)
  
  const allNavItems = [
    { path: '/', label: 'Dashboard', icon: '🏠', menuKey: 'dashboard' },
    { path: '/visit', label: 'Visit', icon: '👤', menuKey: 'visit' },
    { path: '/config', label: 'Configurator', icon: '⚙️', menuKey: 'configurator' },
    { path: '/visits', label: 'Visit History', icon: '📋', menuKey: 'visit_history' },
    { path: '/consent', label: 'Consent Management', icon: '🔐', menuKey: 'consent_management' },
    { path: '/notifications', label: 'Notifications', icon: '🔔', menuKey: 'notifications' },
    { path: '/tasks', label: 'Tasks', icon: '✅', menuKey: 'tasks' },
    { path: '/rbac-test', label: 'RBAC Test', icon: '🛡️', menuKey: 'rbac_test' },
    { path: '/permission-management', label: 'Permission Management', icon: '🔧', menuKey: 'permission_management' }
  ]

  // Fetch user permissions on component mount
  useEffect(() => {
    fetchUserPermissions()
  }, [])

  const fetchUserPermissions = async () => {
    try {
      const response = await api('/policies/user-permissions/')
      console.log('User permissions response:', response)
      setUserPermissions(response)
    } catch (error) {
      console.error('Failed to fetch user permissions:', error)
      // Fallback: show all menus if permission check fails
      const fallbackPermissions = {}
      allNavItems.forEach(item => {
        fallbackPermissions[item.menuKey] = true
      })
      setUserPermissions({ menu_access: fallbackPermissions })
    } finally {
      setLoading(false)
    }
  }

  // Filter nav items based on user permissions
  const getVisibleNavItems = () => {
    if (!userPermissions || !userPermissions.menu_access) {
      return allNavItems // Show all if permissions not loaded
    }

    return allNavItems.filter(item => {
      const canAccess = userPermissions.menu_access[item.menuKey]
      return canAccess === true
    })
  }

  const navItems = getVisibleNavItems()

  const handleLogout = () => {
    // Clear localStorage
    localStorage.removeItem('current_tenant')
    localStorage.removeItem('current_roles')
    localStorage.removeItem('current_departments')
    // Navigate to login
    navigate('/login')
  }

  if (loading) {
    return (
      <div className="app-root">
        <header className="app-header">
          <h1 className="app-title">Hospital POC</h1>
          <TenantSwitcher />
        </header>
        <div className="app-main">
          <div className="loading-container">
            <div className="loading-spinner">⏳</div>
            <p>Loading permissions...</p>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="app-root">
      <header className="app-header">
        <h1 className="app-title">Hospital POC</h1>
        <div className="header-actions">
          <TenantSwitcher onRoleChange={fetchUserPermissions} />
          <button 
            onClick={handleLogout}
            className="logout-button"
            title="Logout"
          >
            🚪 Logout
          </button>
        </div>
      </header>
      <div className="app-main">
        <aside className="app-sidebar">
          <nav className="sidebar-nav">
            {navItems.map((item) => (
              <Link 
                key={item.path}
                to={item.path} 
                className={`nav-link ${location.pathname === item.path ? 'active' : ''}`}
              >
                <span className="nav-icon">{item.icon}</span>
                <span className="nav-label">{item.label}</span>
              </Link>
            ))}
          </nav>
        </aside>
        <main className="app-content">
          {children}
        </main>
      </div>
    </div>
  )
}