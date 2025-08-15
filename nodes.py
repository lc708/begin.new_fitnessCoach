from macore import Node
from utils.call_llm import call_llm, call_llm_with_system
from utils.fitness_knowledge import get_exercises_by_goal_and_level, get_safety_guidelines
from utils.plan_formatter import format_complete_plan
import json
import logging

logger = logging.getLogger(__name__)

class DataValidationNode(Node):
    """
    数据验证节点 - 验证和标准化用户输入的身体数据和健身目标
    """
    
    def prep(self, shared):
        """从shared store读取用户数据"""
        return shared.get('user_data', {})
    
    def exec(self, user_data):
        """验证数据格式，检查数值范围的合理性，标准化数据格式"""
        logger.info("开始验证用户数据")
        
        validated_data = {}
        validation_errors = []
        
        # 验证基础信息
        basic_info = user_data.get('basic_info', {})
        validated_basic = {}
        
        # 年龄验证
        age = basic_info.get('age')
        if age and 16 <= age <= 80:
            validated_basic['age'] = age
        else:
            validation_errors.append("年龄必须在16-80岁之间")
            validated_basic['age'] = 25  # 默认值
        
        # 性别验证
        gender = basic_info.get('gender', '').strip()
        if gender in ['男', '女']:
            validated_basic['gender'] = gender
        else:
            validation_errors.append("请选择性别")
            validated_basic['gender'] = '男'  # 默认值
        
        # 身高验证
        height = basic_info.get('height')
        if height and 140 <= height <= 220:
            validated_basic['height'] = height
        else:
            validation_errors.append("身高必须在140-220cm之间")
            validated_basic['height'] = 170  # 默认值
        
        # 体重验证
        weight = basic_info.get('weight')
        if weight and 40 <= weight <= 200:
            validated_basic['weight'] = weight
        else:
            validation_errors.append("体重必须在40-200kg之间")
            validated_basic['weight'] = 65  # 默认值
        
        # 经验验证
        experience = basic_info.get('experience', '').strip()
        if experience in ['beginner', 'intermediate', 'advanced']:
            validated_basic['experience'] = experience
        else:
            validated_basic['experience'] = 'beginner'  # 默认为初学者
        
        validated_data['basic_info'] = validated_basic
        
        # 验证健身目标
        goals = user_data.get('goals', {})
        validated_goals = {}
        
        primary_goal = goals.get('primary_goal', '').strip()
        valid_goals = ['weight_loss', 'muscle_gain', 'strength', 'endurance', 'toning']
        if primary_goal in valid_goals:
            validated_goals['primary_goal'] = primary_goal
        else:
            validated_goals['primary_goal'] = 'toning'  # 默认目标
        
        validated_goals['target_areas'] = goals.get('target_areas', ['全身'])
        validated_goals['timeline'] = goals.get('timeline', '4周')
        
        validated_data['goals'] = validated_goals
        
        # 验证时间安排
        schedule = user_data.get('schedule', {})
        validated_schedule = {}
        
        days_per_week = schedule.get('days_per_week', 3)
        if 2 <= days_per_week <= 6:
            validated_schedule['days_per_week'] = days_per_week
        else:
            validated_schedule['days_per_week'] = 3  # 默认每周3次
        
        time_per_session = schedule.get('time_per_session', 45)
        if 20 <= time_per_session <= 120:
            validated_schedule['time_per_session'] = time_per_session
        else:
            validated_schedule['time_per_session'] = 45  # 默认45分钟
        
        validated_data['schedule'] = validated_schedule
        
        # 验证身体限制
        limitations = user_data.get('limitations', {})
        validated_limitations = {
            'injuries': limitations.get('injuries', []),
            'restrictions': limitations.get('restrictions', [])
        }
        validated_data['limitations'] = validated_limitations
        
        logger.info(f"数据验证完成，发现{len(validation_errors)}个问题")
        
        return {
            'validated_data': validated_data,
            'validation_errors': validation_errors,
            'is_valid': len(validation_errors) == 0
        }
    
    def post(self, shared, prep_result, exec_result):
        """更新shared store中的用户数据"""
        shared['user_data'] = exec_result['validated_data']
        shared['validation_errors'] = exec_result['validation_errors']
        shared['data_is_valid'] = exec_result['is_valid']
        
        logger.info("数据验证节点完成，进入目标分析阶段")
        return "goal_analysis"  # 转到目标分析节点

class GoalAnalysisNode(Node):
    """
    目标分析节点 - 基于用户数据分析最适合的训练类型和强度
    """
    
    def prep(self, shared):
        """读取验证后的用户数据"""
        user_data = shared.get('user_data', {})
        is_valid = shared.get('data_is_valid', True)
        return user_data, is_valid
    
    def exec(self, inputs):
        """调用LLM分析用户的健身水平和需求，确定训练策略"""
        user_data, is_valid = inputs
        
        if not is_valid:
            logger.warning("数据验证未通过，使用默认分析结果")
            return self._get_default_analysis()
        
        logger.info("开始分析用户目标和制定训练策略")
        
        # 构建分析提示
        basic_info = user_data['basic_info']
        goals = user_data['goals']
        schedule = user_data['schedule']
        limitations = user_data['limitations']
        
        # 计算BMI
        height_m = basic_info['height'] / 100
        bmi = round(basic_info['weight'] / (height_m ** 2), 1)
        
        system_prompt = """你是一位专业的健身教练和运动科学专家。请基于用户的身体数据和目标，分析最适合的训练策略。

请以JSON格式返回分析结果，包含以下字段：
{
  "fitness_level": "评估的健身水平 (初级/中级/高级)",
  "recommended_intensity": "推荐训练强度 (低强度/中等强度/高强度)",
  "suitable_exercise_types": ["适合的运动类型列表"],
  "risk_factors": ["需要注意的风险因素"],
  "training_focus": "主要训练重点",
  "weekly_structure": "建议的周训练结构"
}"""
        
        user_prompt = f"""
用户信息：
- 基础信息：{basic_info['age']}岁，{basic_info['gender']}性，身高{basic_info['height']}cm，体重{basic_info['weight']}kg
- BMI: {bmi}
- 运动经验：{basic_info['experience']}
- 主要目标：{goals['primary_goal']}
- 目标部位：{goals.get('target_areas', [])}
- 训练频率：每周{schedule['days_per_week']}次，每次{schedule['time_per_session']}分钟
- 身体限制：{limitations.get('restrictions', [])}
- 伤病史：{limitations.get('injuries', [])}

请分析这位用户的情况，给出专业的训练策略建议。
"""
        
        try:
            response = call_llm_with_system(system_prompt, user_prompt)
            
            # 尝试解析JSON响应
            if '```json' in response:
                json_str = response.split('```json')[1].split('```')[0].strip()
            elif '{' in response:
                json_str = response[response.find('{'):response.rfind('}')+1]
            else:
                json_str = response
            
            analysis_result = json.loads(json_str)
            
            # 验证必要字段
            required_fields = ['fitness_level', 'recommended_intensity', 'suitable_exercise_types', 'risk_factors']
            for field in required_fields:
                if field not in analysis_result:
                    analysis_result[field] = self._get_default_value(field)
            
            logger.info("目标分析完成")
            return analysis_result
            
        except Exception as e:
            logger.error(f"目标分析出错: {e}")
            return self._get_default_analysis()
    
    def _get_default_analysis(self):
        """获取默认分析结果"""
        return {
            "fitness_level": "初级",
            "recommended_intensity": "中等强度",
            "suitable_exercise_types": ["自重训练", "有氧运动", "核心训练"],
            "risk_factors": ["初学者需要循序渐进"],
            "training_focus": "全身基础训练",
            "weekly_structure": "每周3次全身训练"
        }
    
    def _get_default_value(self, field):
        """获取字段默认值"""
        defaults = {
            'fitness_level': '初级',
            'recommended_intensity': '中等强度',
            'suitable_exercise_types': ['自重训练'],
            'risk_factors': ['注意循序渐进']
        }
        return defaults.get(field, '')
    
    def post(self, shared, prep_result, exec_result):
        """写入分析结果到shared store"""
        shared['analysis_result'] = exec_result
        logger.info("目标分析节点完成，进入计划生成阶段")
        return "plan_generation"  # 转到计划生成节点

class PlanGenerationNode(Node):
    """
    计划生成节点 - 根据分析结果生成具体的训练计划
    """
    
    def prep(self, shared):
        """读取用户数据和分析结果"""
        user_data = shared.get('user_data', {})
        analysis_result = shared.get('analysis_result', {})
        return user_data, analysis_result
    
    def exec(self, inputs):
        """调用LLM和健身知识库生成详细训练计划"""
        user_data, analysis_result = inputs
        
        logger.info("开始生成详细训练计划")
        
        # 获取适合的训练动作
        goal = user_data['goals']['primary_goal']
        level = user_data['basic_info']['experience']
        target_areas = user_data['goals'].get('target_areas', [])
        
        exercises = get_exercises_by_goal_and_level(goal, level, target_areas)
        safety_guidelines = get_safety_guidelines()
        
        # 构建计划生成提示
        system_prompt = f"""你是专业健身教练。生成训练计划必须严格遵守：
- 每周{user_data['schedule']['days_per_week']}次训练
- 每次{user_data['schedule']['time_per_session']}分钟
- 适合{level}水平
- 目标：{goal}

必须返回严格的JSON格式，结构如下：
{{
  "plan_title": "计划标题",
  "overview": {{
    "description": "计划概述",
    "principles": ["训练原则1", "训练原则2"]
  }},
  "weekly_plan": {{
    "total_days": {user_data['schedule']['days_per_week']},
    "session_duration": {user_data['schedule']['time_per_session']},
    "rest_days": "休息日安排"
  }},
  "daily_workouts": [
    {{
      "day": 1,
      "title": "训练日标题",
      "focus": "训练重点",
      "warm_up": {{
        "duration": 5,
        "exercises": ["热身动作1", "热身动作2"]
      }},
      "main_exercises": [
        {{
          "name": "动作名称",
          "target_muscles": ["目标肌群1", "目标肌群2"],
          "sets": 3,
          "reps": "8-12",
          "rest": "60秒",
          "description": "动作要领",
          "tips": ["技巧1", "技巧2"]
        }}
      ],
      "cool_down": {{
        "duration": 5,
        "exercises": ["拉伸动作1", "拉伸动作2"]
      }}
    }}
  ],
  "progression": {{
    "week1": "第一周要点",
    "week2": "第二周要点",
    "week3": "第三周要点",
    "week4": "第四周要点"
  }},
  "nutrition_tips": ["营养建议1", "营养建议2"],
  "safety_reminders": ["安全提醒1", "安全提醒2"]
}}

只返回有效的JSON，不要有任何其他文字说明。"""
        
        # 调试：打印用户的时间安排
        logger.info(f"用户选择的训练频率: 每周{user_data['schedule']['days_per_week']}次")
        logger.info(f"用户选择的训练时长: 每次{user_data['schedule']['time_per_session']}分钟")
        
        user_prompt = f"""用户信息：
- 年龄：{user_data['basic_info']['age']}岁
- 性别：{user_data['basic_info']['gender']}
- 身高：{user_data['basic_info']['height']}cm
- 体重：{user_data['basic_info']['weight']}kg
- 经验：{user_data['basic_info']['experience']}
- 目标：{user_data['goals']['primary_goal']}
- 限制：{user_data['limitations'].get('restrictions', [])}

请生成符合以上JSON格式的训练计划。"""
        
        try:
            raw_plan = call_llm_with_system(system_prompt, user_prompt)
            logger.info("训练计划生成完成")
            
            return {
                'raw_plan_text': raw_plan,
                'available_exercises': exercises,
                'safety_guidelines': safety_guidelines,
                'generation_success': True
            }
            
        except Exception as e:
            logger.error(f"计划生成出错: {e}")
            
            # 生成基础计划作为后备
            backup_plan = self._generate_backup_plan(user_data, analysis_result)
            return {
                'raw_plan_text': backup_plan,
                'available_exercises': exercises,
                'safety_guidelines': safety_guidelines,
                'generation_success': False
            }
    
    def _generate_backup_plan(self, user_data, analysis_result):
        """生成基础后备计划"""
        goal = user_data['goals']['primary_goal']
        level = user_data['basic_info']['experience']
        frequency = user_data['schedule']['days_per_week']
        session_time = user_data['schedule']['time_per_session']
        
        goal_names = {
            'weight_loss': '减脂塑形',
            'muscle_gain': '增肌塑体',
            'strength': '力量提升',
            'endurance': '耐力增强',
            'toning': '身体塑形'
        }
        
        logger.warning(f"使用后备计划：每周{frequency}次，每次{session_time}分钟")
        
        plan_text = f"""
# {goal_names.get(goal, '健身')}训练计划

## 计划概述
这是一份为{level}水平制定的{goal_names.get(goal, '健身')}计划，每周训练{frequency}次，每次{session_time}分钟。

**重要提醒：这是后备简化计划，建议稍后重试以获得更详细的个性化计划。**

## 训练原则
1. 循序渐进，重视动作质量
2. 合理安排休息，避免过度训练
3. 注意饮食和睡眠配合
4. 有问题及时调整

## 周训练安排
根据您选择的每周{frequency}次、每次{session_time}分钟的时间安排：
- 训练频率：每周{frequency}天
- 每次时长：{session_time}分钟
- 训练强度：适合{level}水平

## 注意事项
- 请遵循您设定的时间安排：每周{frequency}次，每次{session_time}分钟
- 建议稍后重试以获得更详细的个性化训练计划
- 如需专业指导，请咨询健身教练

训练内容将包含适合您水平的动作，确保安全有效。
"""
        
        return plan_text
    
    def post(self, shared, prep_result, exec_result):
        """写入生成的计划到shared store"""
        shared['raw_plan'] = exec_result
        logger.info("计划生成节点完成，进入计划优化阶段")
        return "plan_optimization"  # 转到计划优化节点

class PlanOptimizationNode(Node):
    """
    计划优化节点 - 对生成的计划进行安全性检查、个性化调整和格式化
    """
    
    def prep(self, shared):
        """读取原始计划和用户数据"""
        raw_plan = shared.get('raw_plan', {})
        user_data = shared.get('user_data', {})
        return raw_plan, user_data
    
    def exec(self, inputs):
        """调用plan_formatter优化计划，添加安全提醒和免责声明"""
        raw_plan, user_data = inputs
        
        logger.info("开始优化和格式化训练计划")
        
        try:
            # 格式化完整计划
            formatted_plan = format_complete_plan(
                raw_plan.get('raw_plan_text', ''), 
                user_data
            )
            
            # 添加额外的安全检查
            safety_notes = self._add_safety_checks(user_data, formatted_plan)
            formatted_plan['safety_notes'].extend(safety_notes)
            
            # 添加个性化建议
            personal_tips = self._generate_personal_tips(user_data)
            formatted_plan['tips'].extend(personal_tips)
            
            logger.info("计划优化完成")
            
            return {
                'formatted_plan': formatted_plan,
                'optimization_success': True,
                'final_status': 'completed'
            }
            
        except Exception as e:
            logger.error(f"计划优化出错: {e}")
            
            # 创建基础格式化计划
            basic_plan = self._create_basic_formatted_plan(raw_plan, user_data)
            return {
                'formatted_plan': basic_plan,
                'optimization_success': False,
                'final_status': 'completed_with_errors'
            }
    
    def _add_safety_checks(self, user_data, plan):
        """添加针对性安全检查"""
        safety_notes = []
        
        # 检查年龄相关风险
        age = user_data['basic_info']['age']
        if age < 18:
            safety_notes.append("⚠️ 未成年人训练需要成人监护")
        elif age > 50:
            safety_notes.append("⚠️ 建议训练前进行体检，确认身体状况")
        
        # 检查BMI相关风险
        height_m = user_data['basic_info']['height'] / 100
        weight = user_data['basic_info']['weight']
        bmi = weight / (height_m ** 2)
        
        if bmi < 18.5:
            safety_notes.append("⚠️ BMI偏低，建议增加营养摄入，训练强度适中")
        elif bmi > 28:
            safety_notes.append("⚠️ BMI偏高，建议优先选择低冲击运动，循序渐进")
        
        # 检查训练频率风险
        frequency = user_data['schedule']['days_per_week']
        if frequency > 5:
            safety_notes.append("⚠️ 训练频率较高，务必保证充足恢复时间")
        
        return safety_notes
    
    def _generate_personal_tips(self, user_data):
        """生成个性化建议"""
        tips = []
        
        goal = user_data['goals']['primary_goal']
        experience = user_data['basic_info']['experience']
        
        # 根据目标添加建议
        if goal == 'weight_loss':
            tips.append("💡 减脂关键在于创造热量缺口，配合有氧运动效果更佳")
        elif goal == 'muscle_gain':
            tips.append("💡 增肌需要充足蛋白质摄入，建议每公斤体重1.5-2g蛋白质")
        elif goal == 'strength':
            tips.append("💡 力量训练重视渐进式负荷，逐步增加重量和强度")
        
        # 根据经验添加建议
        if experience == 'beginner':
            tips.append("🔰 初学者前4周重点掌握动作要领，不要急于增加重量")
        
        return tips
    
    def _create_basic_formatted_plan(self, raw_plan, user_data):
        """创建基础格式化计划"""
        from utils.fitness_knowledge import get_disclaimer
        
        return {
            'overview': {
                'title': f"个性化健身计划 - {user_data['goals']['primary_goal']}",
                'created_date': "刚刚",
                'description': raw_plan.get('raw_plan_text', '个性化训练计划')
            },
            'user_profile': user_data,
            'plan_content': raw_plan.get('raw_plan_text', ''),
            'safety_notes': ["请注意训练安全", "循序渐进进行"],
            'disclaimer': get_disclaimer(),
            'tips': ["建议截图保存此计划"]
        }
    
    def post(self, shared, prep_result, exec_result):
        """写入最终计划到shared store"""
        shared['final_plan'] = exec_result
        shared['generation_completed'] = True
        
        logger.info("训练计划生成流程全部完成")
        return None  # 流程结束