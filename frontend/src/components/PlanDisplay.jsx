const PlanDisplay = ({ plan }) => {
  if (!plan) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500">暂无训练计划数据</p>
      </div>
    )
  }

  const { overview, user_profile, weekly_schedule, daily_plans, safety_notes, disclaimer, tips } = plan

  return (
    <div className="space-y-8">
      {/* Plan Overview */}
      {overview && (
        <div className="card">
          <div className="text-center mb-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-2">
              {overview.title || '个性化训练计划'}
            </h2>
            <p className="text-gray-600">
              {overview.subtitle || overview.description}
            </p>
            <div className="flex flex-wrap justify-center gap-4 mt-4 text-sm text-gray-500">
              <span>📅 {overview.duration || '4周计划'}</span>
              <span>🔄 {overview.frequency || '每周3次'}</span>
              <span>⏱️ {overview.session_time || '45分钟'}</span>
              <span>📊 {overview.created_date}</span>
            </div>
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
                <div className="font-medium text-gray-900">{String(value)}</div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Weekly Schedule */}
      {weekly_schedule && (
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">📅 周训练安排</h3>
          <div className="grid gap-3">
            {Object.entries(weekly_schedule).map(([day, content]) => (
              <div key={day} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                <span className="font-medium text-gray-900">{day}</span>
                <span className="text-gray-600">{content}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Daily Plans */}
      {daily_plans && daily_plans.length > 0 && (
        <div className="card">
          <h3 className="text-xl font-semibold text-gray-900 mb-4">📋 详细训练计划</h3>
          <div className="space-y-6">
            {daily_plans.map((dayPlan, index) => (
              <div key={index} className="border border-gray-200 rounded-lg p-4">
                <div className="flex items-center justify-between mb-4">
                  <h4 className="text-lg font-semibold text-gray-900">
                    {dayPlan.day} - {dayPlan.focus}
                  </h4>
                  <span className="text-sm text-gray-500">
                    总时长: {dayPlan.total_time}分钟
                  </span>
                </div>

                {/* Warm Up */}
                {dayPlan.warm_up && (
                  <div className="mb-4">
                    <h5 className="font-medium text-gray-900 mb-2">🔥 热身 ({dayPlan.warm_up.duration}分钟)</h5>
                    <ul className="text-sm text-gray-600 space-y-1">
                      {dayPlan.warm_up.exercises.map((exercise, idx) => (
                        <li key={idx}>• {exercise}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Main Workout */}
                {dayPlan.main_workout && dayPlan.main_workout.length > 0 && (
                  <div className="mb-4">
                    <h5 className="font-medium text-gray-900 mb-3">💪 主要训练</h5>
                    <div className="space-y-3">
                      {dayPlan.main_workout.map((exercise, idx) => (
                        <div key={idx} className="bg-gray-50 rounded-lg p-3">
                          <div className="flex items-start justify-between mb-2">
                            <h6 className="font-medium text-gray-900">
                              {exercise.order}. {exercise.name}
                            </h6>
                            <span className="text-xs bg-primary-100 text-primary-700 px-2 py-1 rounded">
                              {exercise.equipment}
                            </span>
                          </div>
                          <div className="grid grid-cols-3 gap-4 text-sm text-gray-600 mb-2">
                            <div>组数: {exercise.sets}</div>
                            <div>次数: {exercise.reps}</div>
                            <div>休息: {exercise.rest}</div>
                          </div>
                          {exercise.target_muscles && exercise.target_muscles.length > 0 && (
                            <div className="text-xs text-gray-500 mb-2">
                              目标肌群: {exercise.target_muscles.join(', ')}
                            </div>
                          )}
                          {exercise.description && (
                            <p className="text-sm text-gray-600 mb-2">{exercise.description}</p>
                          )}
                          {exercise.tips && exercise.tips.length > 0 && (
                            <details className="text-sm">
                              <summary className="cursor-pointer text-primary-600 hover:text-primary-700">
                                动作要点
                              </summary>
                              <ul className="mt-2 space-y-1 text-gray-600">
                                {exercise.tips.map((tip, tipIdx) => (
                                  <li key={tipIdx}>• {tip}</li>
                                ))}
                              </ul>
                            </details>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Cool Down */}
                {dayPlan.cool_down && (
                  <div>
                    <h5 className="font-medium text-gray-900 mb-2">🧘 拉伸放松 ({dayPlan.cool_down.duration}分钟)</h5>
                    <ul className="text-sm text-gray-600 space-y-1">
                      {dayPlan.cool_down.exercises.map((exercise, idx) => (
                        <li key={idx}>• {exercise}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ))}
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

      {/* Safety Notes */}
      {safety_notes && safety_notes.length > 0 && (
        <div className="card border-amber-200 bg-amber-50">
          <h3 className="text-xl font-semibold text-amber-900 mb-4">⚠️ 安全提醒</h3>
          <ul className="space-y-2">
            {safety_notes.map((note, index) => (
              <li key={index} className="flex items-start space-x-2">
                <span className="text-amber-600 mt-1">•</span>
                <span className="text-amber-800">{note}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Disclaimer */}
      {disclaimer && (
        <div className="card border-red-200 bg-red-50">
          <h3 className="text-xl font-semibold text-red-900 mb-4">📋 免责声明</h3>
          <div className="text-red-800 text-sm whitespace-pre-line">
            {disclaimer}
          </div>
        </div>
      )}
    </div>
  )
}

export default PlanDisplay
