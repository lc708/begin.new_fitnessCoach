import { useState } from 'react'

const UserDataForm = ({ onSubmit, currentStep, setCurrentStep }) => {
  const [formData, setFormData] = useState({
    basic_info: {
      age: '',
      gender: '',
      height: '',
      weight: '',
      experience: ''
    },
    goals: {
      primary_goal: '',
      target_areas: [],
      timeline: '4周'
    },
    schedule: {
      days_per_week: 3,
      time_per_session: 45
    },
    limitations: {
      injuries: [],
      restrictions: []
    }
  })

  const [errors, setErrors] = useState({})

  const goalOptions = [
    { value: 'weight_loss', label: '减脂塑形', desc: '减少体脂，塑造身形' },
    { value: 'muscle_gain', label: '增肌塑体', desc: '增加肌肉量，提升力量' },
    { value: 'strength', label: '力量提升', desc: '提高最大力量和爆发力' },
    { value: 'endurance', label: '耐力增强', desc: '提升心肺功能和持久力' },
    { value: 'toning', label: '身体塑形', desc: '塑造身体线条，维持健康' }
  ]

  const experienceOptions = [
    { value: 'beginner', label: '初学者', desc: '0-6个月健身经验' },
    { value: 'intermediate', label: '有经验', desc: '6个月-2年健身经验' },
    { value: 'advanced', label: '高级', desc: '2年以上健身经验' }
  ]

  const targetAreaOptions = [
    '全身', '胸部', '背部', '腿部', '肩部', '手臂', '核心', '有氧'
  ]

  const commonLimitations = [
    '膝盖问题', '腰部问题', '肩部问题', '心血管疾病', '高血压', '糖尿病'
  ]

  const handleInputChange = (section, field, value) => {
    setFormData(prev => ({
      ...prev,
      [section]: {
        ...prev[section],
        [field]: value
      }
    }))
    
    // 清除对应的错误
    if (errors[`${section}.${field}`]) {
      setErrors(prev => ({
        ...prev,
        [`${section}.${field}`]: ''
      }))
    }
  }

  const handleArrayChange = (section, field, value, checked) => {
    setFormData(prev => ({
      ...prev,
      [section]: {
        ...prev[section],
        [field]: checked 
          ? [...prev[section][field], value]
          : prev[section][field].filter(item => item !== value)
      }
    }))
  }

  const validateStep = (step) => {
    const newErrors = {}

    switch (step) {
      case 0: // 基本信息
        if (!formData.basic_info.age || formData.basic_info.age < 16 || formData.basic_info.age > 80) {
          newErrors['basic_info.age'] = '请输入有效年龄 (16-80岁)'
        }
        if (!formData.basic_info.gender) {
          newErrors['basic_info.gender'] = '请选择性别'
        }
        if (!formData.basic_info.height || formData.basic_info.height < 140 || formData.basic_info.height > 220) {
          newErrors['basic_info.height'] = '请输入有效身高 (140-220cm)'
        }
        if (!formData.basic_info.weight || formData.basic_info.weight < 40 || formData.basic_info.weight > 200) {
          newErrors['basic_info.weight'] = '请输入有效体重 (40-200kg)'
        }
        if (!formData.basic_info.experience) {
          newErrors['basic_info.experience'] = '请选择健身经验'
        }
        break

      case 1: // 健身目标
        if (!formData.goals.primary_goal) {
          newErrors['goals.primary_goal'] = '请选择主要健身目标'
        }
        break

      case 2: // 时间安排
        if (!formData.schedule.days_per_week || formData.schedule.days_per_week < 2 || formData.schedule.days_per_week > 6) {
          newErrors['schedule.days_per_week'] = '每周训练天数应在2-6天之间'
        }
        if (!formData.schedule.time_per_session || formData.schedule.time_per_session < 20 || formData.schedule.time_per_session > 120) {
          newErrors['schedule.time_per_session'] = '每次训练时长应在20-120分钟之间'
        }
        break

      case 3: // 身体状况 - 这步是可选的，不需要验证
        break
    }

    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleNext = () => {
    if (validateStep(currentStep)) {
      if (currentStep < 3) {
        setCurrentStep(currentStep + 1)
      } else {
        handleSubmit()
      }
    }
  }

  const handlePrev = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1)
    }
  }

  const handleSubmit = () => {
    // 验证所有步骤
    let allValid = true
    for (let i = 0; i <= 2; i++) {
      if (!validateStep(i)) {
        allValid = false
        break
      }
    }

    if (allValid) {
      // 处理目标部位为空的情况
      const finalData = {
        ...formData,
        goals: {
          ...formData.goals,
          target_areas: formData.goals.target_areas.length > 0 ? formData.goals.target_areas : ['全身']
        }
      }
      onSubmit(finalData)
    } else {
      alert('请检查并完善必填信息')
      setCurrentStep(0) // 回到第一步
    }
  }

  const renderStep = () => {
    switch (currentStep) {
      case 0:
        return (
          <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-900 mb-4">基本信息</h3>
            
            <div className="grid md:grid-cols-2 gap-4">
              <div>
                <label className="form-label">年龄 *</label>
                <input
                  type="number"
                  className={`form-input ${errors['basic_info.age'] ? 'border-red-500' : ''}`}
                  value={formData.basic_info.age}
                  onChange={(e) => handleInputChange('basic_info', 'age', parseInt(e.target.value) || '')}
                  placeholder="请输入年龄"
                  min="16"
                  max="80"
                />
                {errors['basic_info.age'] && <p className="text-red-500 text-sm mt-1">{errors['basic_info.age']}</p>}
              </div>

              <div>
                <label className="form-label">性别 *</label>
                <select
                  className={`form-input ${errors['basic_info.gender'] ? 'border-red-500' : ''}`}
                  value={formData.basic_info.gender}
                  onChange={(e) => handleInputChange('basic_info', 'gender', e.target.value)}
                >
                  <option value="">请选择性别</option>
                  <option value="男">男</option>
                  <option value="女">女</option>
                </select>
                {errors['basic_info.gender'] && <p className="text-red-500 text-sm mt-1">{errors['basic_info.gender']}</p>}
              </div>

              <div>
                <label className="form-label">身高 (cm) *</label>
                <input
                  type="number"
                  className={`form-input ${errors['basic_info.height'] ? 'border-red-500' : ''}`}
                  value={formData.basic_info.height}
                  onChange={(e) => handleInputChange('basic_info', 'height', parseFloat(e.target.value) || '')}
                  placeholder="请输入身高"
                  min="140"
                  max="220"
                />
                {errors['basic_info.height'] && <p className="text-red-500 text-sm mt-1">{errors['basic_info.height']}</p>}
              </div>

              <div>
                <label className="form-label">体重 (kg) *</label>
                <input
                  type="number"
                  className={`form-input ${errors['basic_info.weight'] ? 'border-red-500' : ''}`}
                  value={formData.basic_info.weight}
                  onChange={(e) => handleInputChange('basic_info', 'weight', parseFloat(e.target.value) || '')}
                  placeholder="请输入体重"
                  min="40"
                  max="200"
                />
                {errors['basic_info.weight'] && <p className="text-red-500 text-sm mt-1">{errors['basic_info.weight']}</p>}
              </div>
            </div>

            <div>
              <label className="form-label">健身经验 *</label>
              <div className="grid gap-3">
                {experienceOptions.map(option => (
                  <label key={option.value} className={`flex items-center p-3 border rounded-lg cursor-pointer transition-colors ${
                    formData.basic_info.experience === option.value 
                      ? 'border-primary-500 bg-primary-50' 
                      : 'border-gray-300 hover:border-gray-400'
                  }`}>
                    <input
                      type="radio"
                      name="experience"
                      value={option.value}
                      checked={formData.basic_info.experience === option.value}
                      onChange={(e) => handleInputChange('basic_info', 'experience', e.target.value)}
                      className="text-primary-500 focus:ring-primary-500"
                    />
                    <div className="ml-3">
                      <div className="font-medium">{option.label}</div>
                      <div className="text-sm text-gray-500">{option.desc}</div>
                    </div>
                  </label>
                ))}
              </div>
              {errors['basic_info.experience'] && <p className="text-red-500 text-sm mt-1">{errors['basic_info.experience']}</p>}
            </div>
          </div>
        )

      case 1:
        return (
          <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-900 mb-4">健身目标</h3>
            
            <div>
              <label className="form-label">主要目标 *</label>
              <div className="grid gap-3">
                {goalOptions.map(option => (
                  <label key={option.value} className={`flex items-center p-3 border rounded-lg cursor-pointer transition-colors ${
                    formData.goals.primary_goal === option.value 
                      ? 'border-primary-500 bg-primary-50' 
                      : 'border-gray-300 hover:border-gray-400'
                  }`}>
                    <input
                      type="radio"
                      name="primary_goal"
                      value={option.value}
                      checked={formData.goals.primary_goal === option.value}
                      onChange={(e) => handleInputChange('goals', 'primary_goal', e.target.value)}
                      className="text-primary-500 focus:ring-primary-500"
                    />
                    <div className="ml-3">
                      <div className="font-medium">{option.label}</div>
                      <div className="text-sm text-gray-500">{option.desc}</div>
                    </div>
                  </label>
                ))}
              </div>
              {errors['goals.primary_goal'] && <p className="text-red-500 text-sm mt-1">{errors['goals.primary_goal']}</p>}
            </div>

            <div>
              <label className="form-label">重点训练部位 (可选)</label>
              <p className="text-sm text-gray-500 mb-3">如不选择，将为您安排全身训练</p>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
                {targetAreaOptions.map(area => (
                  <label key={area} className="flex items-center">
                    <input
                      type="checkbox"
                      checked={formData.goals.target_areas.includes(area)}
                      onChange={(e) => handleArrayChange('goals', 'target_areas', area, e.target.checked)}
                      className="text-primary-500 focus:ring-primary-500"
                    />
                    <span className="ml-2 text-sm">{area}</span>
                  </label>
                ))}
              </div>
            </div>
          </div>
        )

      case 2:
        return (
          <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-900 mb-4">时间安排</h3>
            
            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <label className="form-label">每周训练天数 *</label>
                <select
                  className={`form-input ${errors['schedule.days_per_week'] ? 'border-red-500' : ''}`}
                  value={formData.schedule.days_per_week}
                  onChange={(e) => handleInputChange('schedule', 'days_per_week', parseInt(e.target.value))}
                >
                  <option value={2}>每周2天</option>
                  <option value={3}>每周3天</option>
                  <option value={4}>每周4天</option>
                  <option value={5}>每周5天</option>
                  <option value={6}>每周6天</option>
                </select>
                {errors['schedule.days_per_week'] && <p className="text-red-500 text-sm mt-1">{errors['schedule.days_per_week']}</p>}
              </div>

              <div>
                <label className="form-label">每次训练时长 (分钟) *</label>
                <select
                  className={`form-input ${errors['schedule.time_per_session'] ? 'border-red-500' : ''}`}
                  value={formData.schedule.time_per_session}
                  onChange={(e) => handleInputChange('schedule', 'time_per_session', parseInt(e.target.value))}
                >
                  <option value={20}>20分钟</option>
                  <option value={30}>30分钟</option>
                  <option value={45}>45分钟</option>
                  <option value={60}>60分钟</option>
                  <option value={90}>90分钟</option>
                  <option value={120}>120分钟</option>
                </select>
                {errors['schedule.time_per_session'] && <p className="text-red-500 text-sm mt-1">{errors['schedule.time_per_session']}</p>}
              </div>
            </div>

            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <h4 className="font-medium text-blue-900 mb-2">建议</h4>
              <ul className="text-sm text-blue-800 space-y-1">
                <li>• 初学者建议每周3-4次，每次45-60分钟</li>
                <li>• 有经验者可以增加到每周4-5次</li>
                <li>• 确保有足够的休息时间让肌肉恢复</li>
              </ul>
            </div>
          </div>
        )

      case 3:
        return (
          <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-900 mb-4">身体状况</h3>
            
            <div>
              <label className="form-label">身体限制或伤病史 (可选)</label>
              <p className="text-sm text-gray-500 mb-3">如有相关情况，我们会调整训练计划以确保安全</p>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                {commonLimitations.map(limitation => (
                  <label key={limitation} className="flex items-center">
                    <input
                      type="checkbox"
                      checked={formData.limitations.restrictions.includes(limitation)}
                      onChange={(e) => handleArrayChange('limitations', 'restrictions', limitation, e.target.checked)}
                      className="text-primary-500 focus:ring-primary-500"
                    />
                    <span className="ml-2 text-sm">{limitation}</span>
                  </label>
                ))}
              </div>
            </div>

            <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
              <h4 className="font-medium text-amber-900 mb-2">⚠️ 重要提醒</h4>
              <ul className="text-sm text-amber-800 space-y-1">
                <li>• 如有严重疾病或伤势，请先咨询医生</li>
                <li>• 训练过程中如有不适请立即停止</li>
                <li>• 本计划仅供参考，不能替代专业医疗建议</li>
              </ul>
            </div>
          </div>
        )

      default:
        return null
    }
  }

  return (
    <div>
      {renderStep()}
      
      {/* Navigation Buttons */}
      <div className="flex justify-between mt-8 pt-6 border-t border-gray-200">
        <button
          type="button"
          onClick={handlePrev}
          disabled={currentStep === 0}
          className={`px-6 py-2 rounded-lg font-medium transition-colors ${
            currentStep === 0 
              ? 'bg-gray-100 text-gray-400 cursor-not-allowed' 
              : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
          }`}
        >
          上一步
        </button>
        
        <button
          type="button"
          onClick={handleNext}
          className="btn-primary px-6 py-2"
        >
          {currentStep === 3 ? '生成训练计划' : '下一步'}
        </button>
      </div>
    </div>
  )
}

export default UserDataForm
