const LoadingSpinner = () => {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="text-center">
        <div className="inline-block animate-spin rounded-full h-16 w-16 border-4 border-primary-200 border-t-primary-500 mb-4"></div>
        <h2 className="text-2xl font-semibold text-gray-900 mb-2">
          🤖 AI正在为您生成训练计划
        </h2>
        <p className="text-gray-600 mb-6">
          请稍候，正在根据您的个人情况制定专属方案...
        </p>
        
        {/* Loading steps */}
        <div className="max-w-md mx-auto">
          <div className="space-y-3 text-left">
            <div className="flex items-center space-x-3">
              <div className="w-2 h-2 bg-primary-500 rounded-full animate-pulse"></div>
              <span className="text-sm text-gray-600">分析您的身体数据和目标</span>
            </div>
            <div className="flex items-center space-x-3">
              <div className="w-2 h-2 bg-primary-500 rounded-full animate-pulse" style={{animationDelay: '0.2s'}}></div>
              <span className="text-sm text-gray-600">匹配最适合的训练动作</span>
            </div>
            <div className="flex items-center space-x-3">
              <div className="w-2 h-2 bg-primary-500 rounded-full animate-pulse" style={{animationDelay: '0.4s'}}></div>
              <span className="text-sm text-gray-600">制定个性化训练计划</span>
            </div>
            <div className="flex items-center space-x-3">
              <div className="w-2 h-2 bg-primary-500 rounded-full animate-pulse" style={{animationDelay: '0.6s'}}></div>
              <span className="text-sm text-gray-600">添加安全提醒和建议</span>
            </div>
          </div>
        </div>

        <div className="mt-8 text-xs text-gray-500">
          预计需要 10-30 秒，请保持页面开启
        </div>
      </div>
    </div>
  )
}

export default LoadingSpinner
