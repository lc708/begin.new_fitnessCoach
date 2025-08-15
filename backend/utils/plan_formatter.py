"""
训练计划格式化工具 - 将生成的训练计划格式化为用户友好的展示格式
"""
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

def format_weekly_plan(raw_plan: Dict, user_data: Dict) -> Dict:
    """
    格式化周训练计划
    
    Args:
        raw_plan (Dict): 原始训练计划数据
        user_data (Dict): 用户数据
        
    Returns:
        Dict: 格式化后的训练计划
    """
    formatted_plan = {
        "overview": {
            "title": f"个性化训练计划 - {user_data['goals']['primary_goal']}",
            "duration": "4周进阶计划",
            "frequency": f"每周{user_data['schedule']['days_per_week']}次训练",
            "session_time": f"每次约{user_data['schedule']['time_per_session']}分钟",
            "level": user_data['basic_info']['experience'],
            "created_date": datetime.now().strftime("%Y年%m月%d日")
        },
        "weekly_structure": {},
        "daily_plans": [],
        "exercise_library": {},
        "progression_guide": {},
        "notes": []
    }
    
    return formatted_plan

def create_daily_workout(day: int, focus_area: str, exercises: List[Dict], user_level: str) -> Dict:
    """
    创建单日训练计划
    
    Args:
        day (int): 训练日（1-7）
        focus_area (str): 训练重点部位
        exercises (List[Dict]): 训练动作列表
        user_level (str): 用户水平
        
    Returns:
        Dict: 单日训练计划
    """
    # 根据用户水平调整训练参数
    level_params = {
        'beginner': {'sets': (2, 3), 'reps': (8, 12), 'rest': 60},
        'intermediate': {'sets': (3, 4), 'reps': (8, 15), 'rest': 45},
        'advanced': {'sets': (3, 5), 'reps': (6, 15), 'rest': 30}
    }
    
    params = level_params.get(user_level, level_params['beginner'])
    
    daily_plan = {
        "day": f"第{day}天",
        "focus": focus_area,
        "warm_up": {
            "duration": 5,
            "exercises": [
                "动态热身 - 5分钟",
                "关节活动操",
                "轻量级预备动作"
            ]
        },
        "main_workout": [],
        "cool_down": {
            "duration": 5,
            "exercises": [
                "静态拉伸 - 5分钟",
                "深呼吸放松",
                "目标肌群拉伸"
            ]
        },
        "total_time": 0
    }
    
    # 添加主要训练动作
    for i, exercise in enumerate(exercises):
        if i >= 5:  # 限制每天最多5个动作
            break
            
        workout_item = {
            "order": i + 1,
            "name": exercise.get('name', '未知动作'),
            "sets": params['sets'][1] if i < 2 else params['sets'][0],  # 前两个动作多做一组
            "reps": f"{params['reps'][0]}-{params['reps'][1]}",
            "rest": f"{params['rest']}秒",
            "equipment": exercise.get('equipment', '无器械'),
            "target_muscles": exercise.get('primary_muscles', []),
            "description": exercise.get('description', ''),
            "tips": generate_exercise_tips(exercise.get('name', ''), user_level)
        }
        daily_plan["main_workout"].append(workout_item)
    
    # 计算总时间
    main_time = len(daily_plan["main_workout"]) * 3  # 每个动作约3分钟
    daily_plan["total_time"] = daily_plan["warm_up"]["duration"] + main_time + daily_plan["cool_down"]["duration"]
    
    return daily_plan

def generate_exercise_tips(exercise_name: str, level: str) -> List[str]:
    """
    生成动作技巧提示
    
    Args:
        exercise_name (str): 动作名称
        level (str): 用户水平
        
    Returns:
        List[str]: 技巧提示列表
    """
    # 通用提示
    general_tips = {
        "俯卧撑": ["保持身体一条直线", "下降时胸部接近地面", "上升时充分伸展手臂"],
        "深蹲": ["膝盖与脚尖同向", "下蹲时臀部后坐", "保持胸部挺直"],
        "引体向上": ["充分悬垂拉伸", "用背部发力而非手臂", "控制下降速度"],
        "平板支撑": ["保持身体一条直线", "收紧核心肌群", "正常呼吸不憋气"],
        "哑铃弯举": ["肘部固定不摆动", "控制重量缓慢下降", "顶峰收缩停顿"],
        "卷腹": ["下巴微收", "用腹部发力而非颈部", "顶峰停顿1秒"]
    }
    
    # 根据水平添加特殊提示
    level_tips = {
        'beginner': "初学者建议从轻重量开始，重视动作标准性",
        'intermediate': "可适当增加重量，注意肌肉感受",
        'advanced': "可尝试高强度技巧，如慢速负功能"
    }
    
    tips = general_tips.get(exercise_name, ["保持正确姿态", "控制动作节奏", "专注目标肌群发力"])
    
    # 添加水平相关提示
    if level in level_tips:
        tips.append(level_tips[level])
    
    return tips

def create_progression_plan(weeks: int = 4) -> Dict:
    """
    创建进阶计划
    
    Args:
        weeks (int): 计划周数
        
    Returns:
        Dict: 进阶计划
    """
    return {
        "week_1": {
            "focus": "动作学习期",
            "intensity": "60-70%",
            "notes": "重点学习正确动作模式，建立肌肉记忆"
        },
        "week_2": {
            "focus": "适应提高期", 
            "intensity": "70-75%",
            "notes": "在保证动作质量的前提下，适当增加强度"
        },
        "week_3": {
            "focus": "强度增长期",
            "intensity": "75-80%", 
            "notes": "增加训练重量或难度，挑战自我极限"
        },
        "week_4": {
            "focus": "巩固恢复期",
            "intensity": "65-75%",
            "notes": "适当降低强度，巩固训练成果，为下一个周期做准备"
        }
    }

def add_safety_reminders(plan: Dict, user_limitations: List[str]) -> List[str]:
    """
    添加安全提醒
    
    Args:
        plan (Dict): 训练计划
        user_limitations (List[str]): 用户限制条件
        
    Returns:
        List[str]: 安全提醒列表
    """
    safety_notes = [
        "🔥 训练前请进行充分热身，避免运动伤害",
        "💧 训练过程中注意及时补水",
        "⏰ 严格控制组间休息时间，保持训练节奏",
        "🎯 重视动作质量胜过训练重量",
        "🛑 如有任何不适请立即停止训练"
    ]
    
    # 根据用户限制添加特殊提醒
    if "膝盖问题" in user_limitations:
        safety_notes.append("⚠️ 有膝盖问题，请减少深蹲类动作，优先选择上肢训练")
    
    if "腰部问题" in user_limitations:
        safety_notes.append("⚠️ 有腰部问题，避免大重量硬拉，加强核心训练")
    
    if "心血管疾病" in user_limitations:
        safety_notes.append("⚠️ 有心血管疾病，请控制训练强度，必要时咨询医生")
    
    if "高血压" in user_limitations:
        safety_notes.append("⚠️ 有高血压，避免倒立类动作，训练强度循序渐进")
    
    return safety_notes

def format_complete_plan(raw_plan_data: str, user_data: Dict) -> Dict:
    """
    完整格式化训练计划
    
    Args:
        raw_plan_data (str): LLM生成的原始计划文本
        user_data (Dict): 用户数据
        
    Returns:
        Dict: 完整格式化的训练计划
    """
    from .fitness_knowledge import get_disclaimer
    
    # 解析LLM返回的JSON格式训练计划
    try:
        # 清理可能的额外文本，只保留JSON部分
        json_start = raw_plan_data.find('{')
        json_end = raw_plan_data.rfind('}') + 1
        
        if json_start != -1 and json_end > json_start:
            clean_json = raw_plan_data[json_start:json_end]
            parsed_plan = json.loads(clean_json)
            logger.info("成功解析LLM返回的JSON格式训练计划")
        else:
            raise ValueError("未找到有效的JSON格式")
            
    except Exception as e:
        logger.error(f"解析LLM返回的JSON失败: {e}")
        # 创建备用计划结构
        parsed_plan = {
            "plan_title": "备用训练计划",
            "overview": {"description": raw_plan_data[:500] + "..."},
            "daily_workouts": [],
            "weekly_plan": {
                "total_days": user_data['schedule']['days_per_week'],
                "session_duration": user_data['schedule']['time_per_session']
            }
        }
    
    # 创建完整的格式化计划，使用LLM解析后的JSON数据
    formatted_plan = {
        "overview": {
            "title": parsed_plan.get("plan_title", f"🏋️ {user_data['goals']['primary_goal']}专属训练计划"),
            "subtitle": f"适合{user_data['basic_info']['experience']}的个性化方案",
            "duration": "4周进阶计划",
            "frequency": f"每周{user_data['schedule']['days_per_week']}次",
            "session_time": f"每次{user_data['schedule']['time_per_session']}分钟",
            "created_date": datetime.now().strftime("%Y年%m月%d日 %H:%M"),
            "description": parsed_plan.get("overview", {}).get("description", "个性化训练计划"),
            "principles": parsed_plan.get("overview", {}).get("principles", [])
        },
        "user_profile": {
            "基础信息": f"{user_data['basic_info']['age']}岁 {user_data['basic_info']['gender']} "
                       f"{user_data['basic_info']['height']}cm {user_data['basic_info']['weight']}kg",
            "健身经验": user_data['basic_info']['experience'],
            "主要目标": user_data['goals']['primary_goal'],
            "训练频率": f"每周{user_data['schedule']['days_per_week']}次",
            "单次时长": f"{user_data['schedule']['time_per_session']}分钟"
        },
        # 使用LLM生成的结构化数据
        "weekly_plan": parsed_plan.get("weekly_plan", {}),
        "daily_workouts": parsed_plan.get("daily_workouts", []),
        "progression": parsed_plan.get("progression", {}),
        "nutrition_tips": parsed_plan.get("nutrition_tips", []),
        "safety_notes": add_safety_reminders(
            parsed_plan.get("safety_reminders", []), 
            user_data.get('limitations', {}).get('restrictions', [])
        ),
        "disclaimer": get_disclaimer(),
        "tips": [
            "📱 建议截图保存此计划，本应用不保存任何个人信息",
            "📊 建议记录训练数据，跟踪进步情况", 
            "🔄 计划执行4周后可重新评估调整",
            "👨‍⚕️ 如有疑问建议咨询专业健身教练"
        ]
    }
    
    return formatted_plan

def generate_weekly_schedule(user_data: Dict) -> Dict:
    """
    生成周训练安排
    
    Args:
        user_data (Dict): 用户数据
        
    Returns:
        Dict: 周训练安排
    """
    days_per_week = user_data['schedule']['days_per_week']
    goal = user_data['goals']['primary_goal']
    
    # 根据训练频率和目标安排训练内容
    if days_per_week == 3:
        if goal in ['muscle_gain', 'strength']:
            schedule = {
                "周一": "胸部 + 三头肌",
                "周三": "背部 + 二头肌", 
                "周五": "腿部 + 肩部",
                "其他": "休息日（可进行轻度有氧）"
            }
        else:  # weight_loss, toning
            schedule = {
                "周一": "全身力量训练",
                "周三": "有氧 + 核心训练",
                "周五": "下肢 + 臀部训练",
                "其他": "休息日（建议散步等轻度活动）"
            }
    elif days_per_week == 4:
        schedule = {
            "周一": "胸部 + 三头肌",
            "周二": "背部 + 二头肌",
            "周四": "腿部训练",
            "周六": "肩部 + 核心",
            "其他": "休息日"
        }
    elif days_per_week == 5:
        schedule = {
            "周一": "胸部训练",
            "周二": "背部训练", 
            "周三": "腿部训练",
            "周五": "肩部 + 手臂",
            "周六": "核心 + 有氧",
            "其他": "休息日"
        }
    else:  # 默认3天
        schedule = {
            "周一": "上肢训练",
            "周三": "下肢训练",
            "周五": "全身 + 核心",
            "其他": "休息日"
        }
    
    return schedule

def generate_daily_plans(user_data: Dict) -> List[Dict]:
    """
    生成每日训练计划
    
    Args:
        user_data (Dict): 用户数据
        
    Returns:
        List[Dict]: 每日训练计划列表
    """
    from .fitness_knowledge import get_exercises_by_goal_and_level
    
    goal = user_data['goals']['primary_goal']
    level = user_data['basic_info']['experience']
    target_areas = user_data['goals'].get('target_areas', [])
    
    # 获取适合的训练动作
    exercises = get_exercises_by_goal_and_level(goal, level, target_areas)
    
    daily_plans = []
    schedule = generate_weekly_schedule(user_data)
    
    day_counter = 1
    for day, focus in schedule.items():
        if day != "其他":
            # 根据focus确定主要训练部位
            if "胸部" in focus:
                main_exercises = exercises.get('chest', [])
            elif "背部" in focus:
                main_exercises = exercises.get('back', [])
            elif "腿部" in focus:
                main_exercises = exercises.get('legs', [])
            elif "肩部" in focus:
                main_exercises = exercises.get('shoulders', [])
            elif "手臂" in focus:
                main_exercises = exercises.get('arms', [])
            elif "核心" in focus:
                main_exercises = exercises.get('core', [])
            elif "有氧" in focus:
                main_exercises = exercises.get('cardio', [])
            else:
                # 全身训练，混合各部位
                main_exercises = []
                for area in ['legs', 'chest', 'back', 'core']:
                    main_exercises.extend(exercises.get(area, [])[:1])
            
            daily_plan = create_daily_workout(day_counter, focus, main_exercises[:5], level)
            daily_plan["scheduled_day"] = day
            daily_plans.append(daily_plan)
            day_counter += 1
    
    return daily_plans

if __name__ == "__main__":
    # 测试格式化功能
    print("=== 训练计划格式化测试 ===")
    
    # 模拟用户数据
    test_user_data = {
        "basic_info": {"age": 25, "gender": "男", "height": 175, "weight": 70, "experience": "beginner"},
        "goals": {"primary_goal": "muscle_gain", "target_areas": ["chest", "arms"]},
        "schedule": {"days_per_week": 3, "time_per_session": 45},
        "limitations": {"restrictions": ["膝盖问题"]}
    }
    
    # 模拟LLM生成的原始计划
    raw_plan = "针对初学者的增肌计划，重点训练胸部和手臂"
    
    # 格式化计划
    formatted = format_complete_plan(raw_plan, test_user_data)
    
    print("计划概述：")
    print(f"  标题: {formatted['overview']['title']}")
    print(f"  频率: {formatted['overview']['frequency']}")
    print(f"  时长: {formatted['overview']['session_time']}")
    
    print("\n周训练安排：")
    for day, content in formatted['weekly_schedule'].items():
        print(f"  {day}: {content}")
    
    print(f"\n每日计划数量: {len(formatted['daily_plans'])}")
    print(f"安全提醒数量: {len(formatted['safety_notes'])}")
