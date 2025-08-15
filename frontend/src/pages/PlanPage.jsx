import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useUserData } from '../context/UserDataContext'
import PlanDisplay from '../components/PlanDisplay'
import LoadingSpinner from '../components/LoadingSpinner'

const PlanPage = () => {
  const navigate = useNavigate()
  const { generatedPlan, loading, clearData } = useUserData()

  useEffect(() => {
    // 如果没有生成的计划且不在加载中，跳转回表单页
    if (!generatedPlan && !loading) {
      navigate('/form')
    }
  }, [generatedPlan, loading, navigate])

  const handleCreateNew = () => {
    clearData()
    navigate('/form')
  }

  const handleBackHome = () => {
    navigate('/')
  }

  if (loading) {
    return <LoadingSpinner />
  }

  if (!generatedPlan) {
    return null // 将被重定向
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4 max-w-6xl">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            🎉 您的专属训练计划
          </h1>
          <p className="text-gray-600">
            基于您的身体状况和目标量身定制
          </p>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-wrap justify-center gap-4 mb-8">
          <button
            onClick={() => window.print()}
            className="btn-secondary px-6 py-2 text-sm"
          >
            📄 打印计划
          </button>
          <button
            onClick={() => {
              const element = document.querySelector('.plan-content')
              if (element) {
                // 简单的截图提醒
                alert('请使用浏览器的截图功能或手机截屏保存您的训练计划。我们不保存任何个人信息。')
              }
            }}
            className="btn-primary px-6 py-2 text-sm"
          >
            📱 截图保存
          </button>
          <button
            onClick={handleCreateNew}
            className="bg-accent-500 hover:bg-accent-600 text-white font-medium py-2 px-6 rounded-lg transition-colors duration-200 text-sm"
          >
            🔄 重新制定
          </button>
        </div>

        {/* Important Notice */}
        <div className="bg-amber-50 border border-amber-200 rounded-xl p-6 mb-8">
          <div className="flex items-start space-x-3">
            <div className="text-amber-500 text-xl">💾</div>
            <div>
              <h3 className="font-semibold text-amber-800 mb-2">重要提醒</h3>
              <p className="text-amber-700 text-sm mb-2">
                请立即截图或打印保存此计划！我们不保存任何个人信息，刷新页面后计划将丢失。
              </p>
              <p className="text-amber-700 text-sm">
                建议保存到手机相册或打印出来，方便训练时查看。
              </p>
            </div>
          </div>
        </div>

        {/* Plan Display */}
        <div className="plan-content">
          <PlanDisplay plan={generatedPlan} />
        </div>

        {/* Bottom Actions */}
        <div className="text-center mt-12 space-y-4">
          <div className="flex flex-wrap justify-center gap-4">
            <button
              onClick={handleCreateNew}
              className="btn-primary px-8 py-3"
            >
              制定新计划
            </button>
            <button
              onClick={handleBackHome}
              className="bg-gray-500 hover:bg-gray-600 text-white font-medium py-3 px-8 rounded-lg transition-colors duration-200"
            >
              返回首页
            </button>
          </div>
          
          <p className="text-sm text-gray-500">
            感谢使用 FitCoach！祝您训练愉快，早日达成目标！🏆
          </p>
        </div>
      </div>
    </div>
  )
}

export default PlanPage
