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
            <div className="flex items-center justify-center mb-4">
              <h1 className="text-5xl md:text-6xl font-bold text-gray-900">
                🏋️ FitCoach
              </h1>
              {/* GitHub 仓库链接 */}
              <a 
                href="https://github.com/lc708/begin.new_fitnessCoach" 
                target="_blank" 
                rel="noopener noreferrer"
                className="ml-4 p-2 text-gray-600 hover:text-gray-900 transition-colors"
                title="查看GitHub仓库"
              >
                <svg className="w-8 h-8" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
              </a>
            </div>
            <p className="text-sm text-gray-500 mb-4">
              <a href="https://www.begin.new/" target="_blank" rel="noopener noreferrer" className="hover:text-primary-600 transition-colors">powered by begin.new</a>
            </p>
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
          <p className="mb-2">© 2025 FitCoach - 个性化健身训练计划生成器</p>
          <p className="text-sm text-gray-500">
            基于AI技术，为您提供专业的健身指导 • 完全免费 • 保护隐私 • <a href="https://www.begin.new/" target="_blank" rel="noopener noreferrer" className="hover:text-gray-300 transition-colors">powered by begin.new</a>
          </p>
        </div>
      </footer>
    </div>
  )
}

export default HomePage
