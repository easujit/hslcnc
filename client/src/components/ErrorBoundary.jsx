import React from 'react'

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false, error: null, errorInfo: null }
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { hasError: true, error: error }
  }

  componentDidCatch(error, errorInfo) {
    // You can also log the error to an error reporting service
    console.error("ErrorBoundary caught an error:", error, errorInfo)
    this.setState({ errorInfo: errorInfo })
  }

  handleReload = () => {
    window.location.reload()
  }

  handleGoHome = () => {
    window.location.href = '/' // Or '/login' depending on desired behavior
  }

  render() {
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return (
        <div className="error-boundary">
          <div className="error-content">
            <h2>Oops! Something went wrong.</h2>
            <p>We're sorry, but an unexpected error occurred. Please try one of the options below.</p>
            <div className="error-actions">
              <button className="btn" onClick={this.handleReload}>Reload Page</button>
              <button className="btn btn-secondary" onClick={this.handleGoHome}>Go to Home</button>
            </div>
            {this.state.errorInfo && (
              <div className="error-details">
                <details>
                  <summary>Error Details</summary>
                  <pre className="error-stack">
                    {this.state.error && this.state.error.toString()}
                    <br />
                    {this.state.errorInfo.componentStack}
                  </pre>
                </details>
              </div>
            )}
          </div>
        </div>
      )
    }

    return this.props.children
  }
}

export default ErrorBoundary
