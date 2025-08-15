const PlanDisplay = ({ plan }) => {
  if (!plan) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500">暂无训练计划数据</p>
      </div>
    )
  }

  // 英文到中文的映射
  const translateValue = (value) => {
    const translations = {
      // 经验水平
      'beginner': '初学者',
      'intermediate': '中级',
      'advanced': '高级',
      // 健身目标
      'weight_loss': '减脂',
      'muscle_gain': '增肌',
      'strength': '力量训练',
      'endurance': '耐力训练',
      'flexibility': '柔韧性',
      'general_fitness': '综合健身',
      // 其他常见英文
      'male': '男',
      'female': '女'
    }
    return translations[value] || value
  }

  const { overview, user_profile, weekly_plan, daily_workouts, progression, nutrition_tips, safety_notes, disclaimer, tips } = plan

  return (
    <div className="space-y-8">
      {/* Plan Overview */}
      {overview && (
        <div className="card">
          <div className="text-center mb-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-2">
              {overview.title || '个性化训练计划'}
            </h2>
            <p className="text-gray-600 mb-4">
              {overview.subtitle}
            </p>
            {overview.description && (
              <p className="text-gray-700 mb-4 text-left">
                {overview.description}
              </p>
            )}
            <div className="flex flex-wrap justify-center gap-4 mt-4 text-sm text-gray-500">
              <span>📅 {overview.duration || '4周计划'}</span>
              <span>🔄 {overview.frequency || '用户定制'}</span>
              <span>⏱️ {overview.session_time || '用户定制'}</span>
              <span>📊 {overview.created_date}</span>
            </div>
            
            {/* Training Principles */}
            {overview.principles && overview.principles.length > 0 && (
              <div className="mt-6">
                <h4 className="text-lg font-semibold text-gray-900 mb-3">🎯 训练原则</h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {overview.principles.map((principle, index) => (
                    <div key={index} className="bg-blue-50 p-3 rounded-lg">
                      <p className="text-blue-800 text-sm">{principle}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Weekly Plan Summary */}
      {weekly_plan && (
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">📊 训练安排概览</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-green-50 p-4 rounded-lg text-center">
              <div className="text-2xl font-bold text-green-600">{weekly_plan.total_days || 3}</div>
              <div className="text-green-800 text-sm">每周训练次数</div>
            </div>
            <div className="bg-blue-50 p-4 rounded-lg text-center">
              <div className="text-2xl font-bold text-blue-600">{weekly_plan.session_duration || 45}</div>
              <div className="text-blue-800 text-sm">每次训练时长(分钟)</div>
            </div>
            <div className="bg-purple-50 p-4 rounded-lg text-center">
              <div className="text-purple-600 text-sm">{weekly_plan.rest_days || '其他日期为休息日'}</div>
            </div>
          </div>
        </div>
      )}

      {/* Daily Workouts */}
      {daily_workouts && daily_workouts.length > 0 && (
        <div className="space-y-6">
          <h3 className="text-xl font-semibold text-gray-900 text-center">🏋️ 每日训练详情</h3>
          {daily_workouts.map((workout, index) => (
            <div key={index} className="card">
              <div className="border-l-4 border-indigo-500 pl-4 mb-4">
                <h4 className="text-lg font-bold text-gray-900">
                  第{workout.day}天: {workout.title}
                </h4>
                <p className="text-indigo-600">{workout.focus}</p>
              </div>

              {/* Warm-up */}
              {workout.warm_up && (
                <div className="mb-6">
                  <h5 className="font-semibold text-gray-800 mb-2 flex items-center">
                    🔥 热身运动 ({workout.warm_up.duration}分钟)
                  </h5>
                  <div className="bg-orange-50 p-3 rounded-lg">
                    <ul className="list-disc list-inside space-y-1">
                      {workout.warm_up.exercises.map((exercise, i) => (
                        <li key={i} className="text-orange-800 text-sm">{exercise}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              )}

              {/* Main Exercises */}
              {workout.main_exercises && workout.main_exercises.length > 0 && (
                <div className="mb-6">
                  <h5 className="font-semibold text-gray-800 mb-3">💪 主要训练</h5>
                  <div className="space-y-4">
                    {workout.main_exercises.map((exercise, i) => (
                      <div key={i} className="border border-gray-200 rounded-lg p-4">
                        <div className="flex flex-wrap items-center justify-between mb-2">
                          <h6 className="font-semibold text-gray-900">{exercise.name}</h6>
                          <div className="flex space-x-4 text-sm text-gray-600">
                            <span>🔢 {exercise.sets}组</span>
                            <span>🔄 {exercise.reps}次</span>
                            <span>⏱️ 休息{exercise.rest}</span>
                          </div>
                        </div>
                        
                        {exercise.target_muscles && exercise.target_muscles.length > 0 && (
                          <div className="mb-2">
                            <span className="text-sm text-gray-600">目标肌群: </span>
                            {exercise.target_muscles.map((muscle, mi) => (
                              <span key={mi} className="inline-block bg-gray-100 text-gray-700 text-xs px-2 py-1 rounded mr-1">
                                {muscle}
                              </span>
                            ))}
                          </div>
                        )}
                        
                        {exercise.description && (
                          <p className="text-gray-700 text-sm mb-2">{exercise.description}</p>
                        )}
                        
                        {exercise.tips && exercise.tips.length > 0 && (
                          <div className="bg-yellow-50 p-2 rounded">
                            <h7 className="text-xs font-semibold text-yellow-800">💡 技巧提示:</h7>
                            <ul className="list-disc list-inside space-y-1 mt-1">
                              {exercise.tips.map((tip, ti) => (
                                <li key={ti} className="text-yellow-700 text-xs">{tip}</li>
                              ))}
                            </ul>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Cool-down */}
              {workout.cool_down && (
                <div className="mb-4">
                  <h5 className="font-semibold text-gray-800 mb-2 flex items-center">
                    🧘 拉伸放松 ({workout.cool_down.duration}分钟)
                  </h5>
                  <div className="bg-green-50 p-3 rounded-lg">
                    <ul className="list-disc list-inside space-y-1">
                      {workout.cool_down.exercises.map((exercise, i) => (
                        <li key={i} className="text-green-800 text-sm">{exercise}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Progression Plan */}
      {progression && Object.keys(progression).length > 0 && (
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">📈 进阶计划</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {Object.entries(progression).map(([week, plan]) => (
              <div key={week} className="bg-gradient-to-br from-purple-50 to-indigo-50 p-4 rounded-lg">
                <h4 className="font-semibold text-purple-900 mb-2">{week}</h4>
                <p className="text-purple-700 text-sm">{plan}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Nutrition Tips */}
      {nutrition_tips && nutrition_tips.length > 0 && (
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">🍎 营养建议</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {nutrition_tips.map((tip, index) => (
              <div key={index} className="bg-green-50 p-3 rounded-lg border-l-4 border-green-400">
                <p className="text-green-800 text-sm">{tip}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* User Profile Summary */}
      {user_profile && (
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">👤 用户档案</h3>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {Object.entries(user_profile).map(([key, value]) => (
              <div key={key} className="bg-gray-50 rounded-lg p-3">
                <div className="text-sm text-gray-600">{key}</div>
                <div className="font-medium text-gray-900">{translateValue(String(value))}</div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Safety Notes */}
      {safety_notes && safety_notes.length > 0 && (
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">⚠️ 安全提醒</h3>
          <div className="bg-red-50 border border-red-200 rounded-lg p-4">
            <ul className="space-y-2">
              {safety_notes.map((note, index) => (
                <li key={index} className="flex items-start space-x-2">
                  <span className="text-red-800 text-sm">{note}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}

      {/* Tips */}
      {tips && tips.length > 0 && (
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">💡 训练建议</h3>
          <ul className="space-y-2">
            {tips.map((tip, index) => (
              <li key={index} className="flex items-start space-x-2">
                <span className="text-primary-500 mt-1">•</span>
                <span className="text-gray-700">{tip}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Disclaimer */}
      {disclaimer && (
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">📋 免责声明</h3>
          <div className="bg-gray-50 border border-gray-200 rounded-lg p-4">
            <p className="text-gray-700 text-sm whitespace-pre-line">{disclaimer}</p>
          </div>
        </div>
      )}
    </div>
  )
}

export default PlanDisplay