import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Analytics } from '@vercel/analytics/react'
import HomePage from './pages/HomePage'
import FormPage from './pages/FormPage'
import PlanPage from './pages/PlanPage'
import { UserDataProvider } from './context/UserDataContext'

function App() {
  return (
    <UserDataProvider>
      <Router>
        <div className="min-h-screen bg-gray-50">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/form" element={<FormPage />} />
            <Route path="/plan" element={<PlanPage />} />
          </Routes>
        </div>
        <Analytics />
      </Router>
    </UserDataProvider>
  )
}

export default App