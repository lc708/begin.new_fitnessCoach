import { useState, useEffect } from 'react'

const LoadingSpinner = () => {
  const [currentTip, setCurrentTip] = useState(0)
  const [progress, setProgress] = useState(0)

  // 健身知识和励志文案
  const fitnessTips = [
    {
      icon: "🎯",
      title: "目标设定的艺术",
      content: "制定具体、可衡量的健身目标是成功的第一步。比如'3个月内增重5公斤'比'想要变强壮'更有效果。",
      category: "心态建设"
    },
    {
      icon: "💪",
      title: "肌肉记忆的秘密",
      content: "坚持训练4-6周，您的神经系统会建立肌肉记忆，动作会变得更自然流畅，这时候真正的进步才刚刚开始。",
      category: "科学知识"
    },
    {
      icon: "🔥",
      title: "热身的重要性",
      content: "充分的热身能将受伤风险降低50%以上，同时提高训练效果。永远不要跳过这关键的5-10分钟。",
      category: "安全提醒"
    },
    {
      icon: "🏃",
      title: "有氧与力量的平衡",
      content: "有氧运动强化心肺，力量训练塑造身材。最佳比例是70%力量训练配合30%有氧运动。",
      category: "训练技巧"
    },
    {
      icon: "💧",
      title: "水分补给法则",
      content: "运动前2小时喝500ml水，运动中每15分钟补充150ml，运动后按体重流失量的150%补充。",
      category: "营养指导"
    },
    {
      icon: "🌙",
      title: "恢复比训练更重要",
      content: "肌肉在休息时生长，不在训练时。确保每晚7-9小时睡眠，让身体充分修复和重建。",
      category: "恢复指导"
    },
    {
      icon: "🧠",
      title: "意念肌肉连接",
      content: "训练时专注感受目标肌肉的收缩，这种'意念肌肉连接'能提高训练效果30%以上。",
      category: "进阶技巧"
    },
    {
      icon: "⚡",
      title: "渐进式负荷原理",
      content: "每周适度增加重量、次数或训练量，让身体持续适应新的挑战，这是进步的根本。",
      category: "训练原理"
    },
    {
      icon: "🍎",
      title: "营养时机的智慧",
      content: "训练后30分钟内是'黄金窗口期'，此时补充蛋白质和碳水化合物，恢复效果最佳。",
      category: "营养时机"
    },
    {
      icon: "🎖️",
      title: "坚持就是胜利",
      content: "研究表明，坚持运动12周以上的人，有85%会将健身变成终生习惯。您已经迈出了最重要的一步！",
      category: "励志鼓励"
    }
  ]

  const encouragements = [
    "🌟 每一次训练都是对未来更好自己的投资",
    "💎 身体是您一生的作品，值得精心雕琢",
    "🚀 今天的汗水，是明天自信的源泉",
    "🏆 强者不是没有恐惧，而是征服恐惧",
    "✨ 改变从决定开始，坚持让奇迹发生"
  ]

  // 轮播效果
  useEffect(() => {
    const tipInterval = setInterval(() => {
      setCurrentTip((prev) => (prev + 1) % fitnessTips.length)
    }, 8000) // 每8秒切换一次

    const progressInterval = setInterval(() => {
      setProgress((prev) => {
        const newProgress = prev + (100 / 60) // 60秒内完成
        return newProgress > 100 ? 100 : newProgress
      })
    }, 1000)

    return () => {
      clearInterval(tipInterval)
      clearInterval(progressInterval)
    }
  }, [])

  const currentTipData = fitnessTips[currentTip]
  const currentEncouragement = encouragements[currentTip % encouragements.length]

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-secondary-50 flex items-center justify-center p-4">
      <div className="max-w-2xl mx-auto text-center">
        {/* 主标题区域 */}
        <div className="mb-8">
          <div className="relative inline-block">
            <div className="absolute inset-0 animate-ping rounded-full bg-primary-200 opacity-30"></div>
            <div className="relative bg-white rounded-full p-6 shadow-lg">
              <div className="text-4xl">🤖</div>
            </div>
          </div>
          <h2 className="text-3xl font-bold text-gray-900 mt-6 mb-3">
            AI正在为您精心制定训练计划
          </h2>
          <p className="text-lg text-gray-600">
            请稍候 30-60 秒，我们正在根据您的个人情况制定专属方案...
          </p>
        </div>

        {/* 进度条 */}
        <div className="mb-8">
          <div className="w-full bg-gray-200 rounded-full h-2 mb-2">
            <div 
              className="bg-gradient-to-r from-primary-500 to-secondary-500 h-2 rounded-full transition-all duration-1000 ease-out"
              style={{ width: `${progress}%` }}
            ></div>
          </div>
          <p className="text-sm text-gray-500">正在分析和生成中...</p>
        </div>

        {/* 健身知识轮播 */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-6">
          <div className="transition-all duration-500 ease-in-out">
            <div className="flex items-center justify-center mb-4">
              <span className="text-4xl mr-3">{currentTipData.icon}</span>
              <span className="text-xs bg-primary-100 text-primary-600 px-3 py-1 rounded-full font-medium">
                {currentTipData.category}
              </span>
            </div>
            <h3 className="text-xl font-semibold text-gray-900 mb-3">
              {currentTipData.title}
            </h3>
            <p className="text-gray-700 leading-relaxed">
              {currentTipData.content}
            </p>
          </div>
        </div>

        {/* 励志文案 */}
        <div className="bg-gradient-to-r from-primary-500 to-secondary-500 rounded-xl p-6 text-white mb-8">
          <p className="text-lg font-medium">{currentEncouragement}</p>
        </div>

        {/* 处理步骤指示器 */}
        <div className="bg-gray-50 rounded-xl p-6">
          <h4 className="text-sm font-medium text-gray-900 mb-4">AI处理进度</h4>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
            {[
              { step: "数据分析", icon: "📊", delay: "0s" },
              { step: "目标匹配", icon: "🎯", delay: "0.2s" },
              { step: "计划生成", icon: "📝", delay: "0.4s" },
              { step: "安全优化", icon: "🛡️", delay: "0.6s" }
            ].map((item, index) => (
              <div key={index} className="text-center">
                <div 
                  className="w-12 h-12 bg-white rounded-full flex items-center justify-center mx-auto mb-2 shadow-sm animate-pulse"
                  style={{ animationDelay: item.delay }}
                >
                  <span className="text-lg">{item.icon}</span>
                </div>
                <span className="text-xs text-gray-600">{item.step}</span>
              </div>
            ))}
          </div>
        </div>

        {/* 底部提示 */}
        <div className="mt-8 text-center">
          <p className="text-sm text-gray-500 mb-2">
            💡 小贴士：请保持页面开启，我们不保存任何个人信息
          </p>
          <div className="flex items-center justify-center space-x-2 text-xs text-gray-400">
            <div className="w-2 h-2 bg-primary-400 rounded-full animate-bounce"></div>
            <div className="w-2 h-2 bg-primary-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
            <div className="w-2 h-2 bg-primary-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default LoadingSpinner
