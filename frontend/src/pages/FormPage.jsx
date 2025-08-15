import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useUserData } from '../context/UserDataContext'
import UserDataForm from '../components/UserDataForm'

const FormPage = () => {
  const navigate = useNavigate()
  const { setUserData, setGeneratedPlan, setLoading } = useUserData()
  const [currentStep, setCurrentStep] = useState(0)

  const handleFormSubmit = async (formData) => {
    try {
      setLoading(true)
      setUserData(formData)

      // 调用API生成训练计划
      const response = await fetch(`${import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'}/api/generate-plan`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })

      const result = await response.json()

      if (result.success) {
        setGeneratedPlan(result.data.plan)
        navigate('/plan')
      } else {
        alert('生成训练计划失败：' + (result.error || '未知错误'))
      }
    } catch (error) {
      console.error('API调用失败:', error)
      alert('网络错误，请检查后端服务是否运行')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4 max-w-4xl">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            📋 个人信息填写
          </h1>
          <p className="text-gray-600">
            请填写您的基本信息，我们将为您生成个性化的训练计划
          </p>
        </div>

        {/* Progress Indicator */}
        <div className="mb-8">
          <div className="flex items-center justify-center space-x-4">
            {[
              { step: 0, title: '基本信息' },
              { step: 1, title: '健身目标' },
              { step: 2, title: '时间安排' },
              { step: 3, title: '身体状况' }
            ].map((item, index) => (
              <div key={index} className="flex items-center">
                <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium ${
                  currentStep >= item.step 
                    ? 'bg-primary-500 text-white' 
                    : 'bg-gray-200 text-gray-500'
                }`}>
                  {item.step + 1}
                </div>
                <span className={`ml-2 text-sm ${
                  currentStep >= item.step ? 'text-primary-600' : 'text-gray-500'
                }`}>
                  {item.title}
                </span>
                {index < 3 && (
                  <div className={`w-8 h-0.5 ml-4 ${
                    currentStep > item.step ? 'bg-primary-500' : 'bg-gray-200'
                  }`}></div>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Main Form */}
        <div className="card">
          <UserDataForm 
            onSubmit={handleFormSubmit}
            currentStep={currentStep}
            setCurrentStep={setCurrentStep}
          />
        </div>

        {/* Back to Home */}
        <div className="text-center mt-8">
          <button
            onClick={() => navigate('/')}
            className="text-gray-500 hover:text-gray-700 text-sm"
          >
            ← 返回首页
          </button>
        </div>
      </div>
    </div>
  )
}

export default FormPage
