import { createContext, useContext, useState } from 'react'

const UserDataContext = createContext()

export const useUserData = () => {
  const context = useContext(UserDataContext)
  if (!context) {
    throw new Error('useUserData must be used within a UserDataProvider')
  }
  return context
}

export const UserDataProvider = ({ children }) => {
  const [userData, setUserData] = useState(null)
  const [generatedPlan, setGeneratedPlan] = useState(null)
  const [loading, setLoading] = useState(false)

  const clearData = () => {
    setUserData(null)
    setGeneratedPlan(null)
  }

  const value = {
    userData,
    setUserData,
    generatedPlan,
    setGeneratedPlan,
    loading,
    setLoading,
    clearData
  }

  return (
    <UserDataContext.Provider value={value}>
      {children}
    </UserDataContext.Provider>
  )
}
