import { Link } from 'react-router-dom'
import { useUserData } from '../context/UserDataContext'

const HomePage = () => {
  const { clearData } = useUserData()

  const features = [
    {
      title: "个性化定制",
      description: "基于您的身体数据和目标",
      icon: "🎯"
    },
    {
      title: "科学安全",
      description: "专业的训练建议和安全提醒",
      icon: "🔬"
    },
    {
      title: "隐私保护",
      description: "不保存任何个人信息",
      icon: "🔒"
    }
  ]

  const handleStartClick = () => {
    clearData() // 清除之前的数据
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 to-secondary-50">
      {/* Hero Section */}
      <div className="container mx-auto px-4 py-16">
        <div className="text-center max-w-4xl mx-auto">
          {/* Logo/Brand */}
          <div className="mb-8">
            <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-4">
              🏋️ FitCoach
            </h1>
            <p className="text-xl md:text-2xl text-gray-600 font-medium">
              AI驱动的个性化健身训练计划
            </p>
          </div>

          {/* Main CTA */}
          <div className="mb-12">
            <p className="text-lg text-gray-700 mb-8 max-w-2xl mx-auto">
              告诉我们您的身体状况和健身目标，我们将为您量身定制专业的训练计划。
              完全免费，无需注册，保护您的隐私。
            </p>
            <Link 
              to="/form" 
              onClick={handleStartClick}
              className="inline-block bg-primary-500 hover:bg-primary-600 text-white font-semibold py-4 px-8 rounded-xl text-lg transition-all duration-200 transform hover:scale-105 shadow-lg"
            >
              开始制定计划 →
            </Link>
          </div>

          {/* Features */}
          <div className="grid md:grid-cols-3 gap-8 mb-16">
            {features.map((feature, index) => (
              <div key={index} className="card text-center">
                <div className="text-4xl mb-4">{feature.icon}</div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">
                  {feature.title}
                </h3>
                <p className="text-gray-600">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>

          {/* How it works */}
          <div className="bg-white rounded-2xl shadow-sm p-8 mb-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-8">如何使用</h2>
            <div className="grid md:grid-cols-4 gap-6">
              <div className="text-center">
                <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-3">
                  <span className="text-primary-600 font-bold">1</span>
                </div>
                <h4 className="font-semibold text-gray-900 mb-2">填写信息</h4>
                <p className="text-sm text-gray-600">输入基本身体数据和健身目标</p>
              </div>
              <div className="text-center">
                <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-3">
                  <span className="text-primary-600 font-bold">2</span>
                </div>
                <h4 className="font-semibold text-gray-900 mb-2">AI分析</h4>
                <p className="text-sm text-gray-600">专业算法分析您的需求</p>
              </div>
              <div className="text-center">
                <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-3">
                  <span className="text-primary-600 font-bold">3</span>
                </div>
                <h4 className="font-semibold text-gray-900 mb-2">生成计划</h4>
                <p className="text-sm text-gray-600">获得个性化训练方案</p>
              </div>
              <div className="text-center">
                <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-3">
                  <span className="text-primary-600 font-bold">4</span>
                </div>
                <h4 className="font-semibold text-gray-900 mb-2">开始训练</h4>
                <p className="text-sm text-gray-600">跟随计划开始健身之旅</p>
              </div>
            </div>
          </div>

          {/* Important Notes */}
          <div className="bg-amber-50 border border-amber-200 rounded-xl p-6">
            <div className="flex items-start space-x-3">
              <div className="text-amber-500 text-xl">⚠️</div>
              <div className="text-left">
                <h3 className="font-semibold text-amber-800 mb-2">重要提醒</h3>
                <ul className="text-sm text-amber-700 space-y-1">
                  <li>• 本应用提供的训练计划仅供参考，不能替代专业健身指导</li>
                  <li>• 开始训练前建议咨询专业教练或医生</li>
                  <li>• 我们不保存任何个人信息，请截图保存您的训练计划</li>
                  <li>• 训练过程中如有不适请立即停止</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-300 py-8">
        <div className="container mx-auto px-4 text-center">
          <p className="mb-2">© 2024 FitCoach - 个性化健身训练计划生成器</p>
          <p className="text-sm text-gray-500">
            基于AI技术，为您提供专业的健身指导 • 完全免费 • 保护隐私
          </p>
        </div>
      </footer>
    </div>
  )
}

export default HomePage
