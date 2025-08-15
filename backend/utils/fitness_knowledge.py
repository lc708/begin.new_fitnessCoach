"""
健身知识库工具 - 提供健身动作数据库和安全指导原则
"""

def get_exercise_database():
    """
    获取健身动作数据库
    
    Returns:
        dict: 包含各类健身动作的数据库
    """
    return {
        "chest": {
            "beginner": [
                {"name": "俯卧撑", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["胸大肌"], "description": "经典的胸部训练动作"},
                {"name": "上斜俯卧撑", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["胸大肌上部"], "description": "脚部抬高的俯卧撑变式"},
                {"name": "哑铃飞鸟", "equipment": "哑铃", "difficulty": "初级", "primary_muscles": ["胸大肌"], "description": "胸部孤立训练动作"}
            ],
            "intermediate": [
                {"name": "杠铃卧推", "equipment": "杠铃", "difficulty": "中级", "primary_muscles": ["胸大肌", "三头肌"], "description": "胸部力量训练经典动作"},
                {"name": "双杠臂屈伸", "equipment": "双杠", "difficulty": "中级", "primary_muscles": ["胸大肌下部", "三头肌"], "description": "上肢复合训练动作"},
                {"name": "哑铃卧推", "equipment": "哑铃", "difficulty": "中级", "primary_muscles": ["胸大肌"], "description": "单边刺激胸部肌肉"}
            ]
        },
        "back": {
            "beginner": [
                {"name": "引体向上", "equipment": "单杠", "difficulty": "中级", "primary_muscles": ["背阔肌"], "description": "背部训练王牌动作"},
                {"name": "哑铃划船", "equipment": "哑铃", "difficulty": "初级", "primary_muscles": ["背阔肌", "菱形肌"], "description": "背部厚度训练"},
                {"name": "弹力带划船", "equipment": "弹力带", "difficulty": "初级", "primary_muscles": ["背阔肌"], "description": "适合初学者的背部训练"}
            ],
            "intermediate": [
                {"name": "杠铃划船", "equipment": "杠铃", "difficulty": "中级", "primary_muscles": ["背阔肌", "菱形肌"], "description": "背部厚度的经典动作"},
                {"name": "高位下拉", "equipment": "器械", "difficulty": "中级", "primary_muscles": ["背阔肌"], "description": "背部宽度训练"},
                {"name": "T杠划船", "equipment": "T杠", "difficulty": "中级", "primary_muscles": ["背阔肌", "菱形肌"], "description": "背部中央厚度训练"}
            ]
        },
        "legs": {
            "beginner": [
                {"name": "深蹲", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["股四头肌", "臀大肌"], "description": "下肢训练之王"},
                {"name": "弓步蹲", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["股四头肌", "臀大肌"], "description": "单腿力量训练"},
                {"name": "臀桥", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["臀大肌", "腘绳肌"], "description": "臀部激活训练"}
            ],
            "intermediate": [
                {"name": "杠铃深蹲", "equipment": "杠铃", "difficulty": "中级", "primary_muscles": ["股四头肌", "臀大肌"], "description": "负重深蹲训练"},
                {"name": "硬拉", "equipment": "杠铃", "difficulty": "中级", "primary_muscles": ["腘绳肌", "臀大肌", "竖脊肌"], "description": "后链力量训练"},
                {"name": "保加利亚分腿蹲", "equipment": "无器械", "difficulty": "中级", "primary_muscles": ["股四头肌", "臀大肌"], "description": "单腿深蹲变式"}
            ]
        },
        "shoulders": {
            "beginner": [
                {"name": "哑铃推举", "equipment": "哑铃", "difficulty": "初级", "primary_muscles": ["三角肌"], "description": "肩部综合训练"},
                {"name": "侧平举", "equipment": "哑铃", "difficulty": "初级", "primary_muscles": ["三角肌中束"], "description": "肩部宽度训练"},
                {"name": "前平举", "equipment": "哑铃", "difficulty": "初级", "primary_muscles": ["三角肌前束"], "description": "肩部前束训练"}
            ],
            "intermediate": [
                {"name": "杠铃推举", "equipment": "杠铃", "difficulty": "中级", "primary_muscles": ["三角肌", "三头肌"], "description": "肩部力量训练"},
                {"name": "反向飞鸟", "equipment": "哑铃", "difficulty": "中级", "primary_muscles": ["三角肌后束"], "description": "肩部后束训练"},
                {"name": "阿诺德推举", "equipment": "哑铃", "difficulty": "中级", "primary_muscles": ["三角肌"], "description": "全方位肩部刺激"}
            ]
        },
        "arms": {
            "beginner": [
                {"name": "哑铃弯举", "equipment": "哑铃", "difficulty": "初级", "primary_muscles": ["肱二头肌"], "description": "二头肌经典训练"},
                {"name": "哑铃臂屈伸", "equipment": "哑铃", "difficulty": "初级", "primary_muscles": ["肱三头肌"], "description": "三头肌孤立训练"},
                {"name": "锤式弯举", "equipment": "哑铃", "difficulty": "初级", "primary_muscles": ["肱二头肌", "肱桡肌"], "description": "手臂整体训练"}
            ],
            "intermediate": [
                {"name": "杠铃弯举", "equipment": "杠铃", "difficulty": "中级", "primary_muscles": ["肱二头肌"], "description": "二头肌力量训练"},
                {"name": "窄距俯卧撑", "equipment": "无器械", "difficulty": "中级", "primary_muscles": ["肱三头肌"], "description": "三头肌复合训练"},
                {"name": "集中弯举", "equipment": "哑铃", "difficulty": "中级", "primary_muscles": ["肱二头肌"], "description": "二头肌精准刺激"}
            ]
        },
        "core": {
            "beginner": [
                {"name": "平板支撑", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["核心肌群"], "description": "核心稳定性训练"},
                {"name": "卷腹", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["腹直肌"], "description": "腹部经典训练"},
                {"name": "侧平板支撑", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["腹斜肌"], "description": "侧腹训练"}
            ],
            "intermediate": [
                {"name": "悬垂举腿", "equipment": "单杠", "difficulty": "中级", "primary_muscles": ["下腹部"], "description": "下腹强化训练"},
                {"name": "俄式转体", "equipment": "无器械", "difficulty": "中级", "primary_muscles": ["腹斜肌"], "description": "腰腹旋转训练"},
                {"name": "死虫子", "equipment": "无器械", "difficulty": "中级", "primary_muscles": ["核心肌群"], "description": "核心控制训练"}
            ]
        },
        "cardio": {
            "beginner": [
                {"name": "快走", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["心肺"], "description": "低冲击有氧运动"},
                {"name": "原地踏步", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["心肺"], "description": "室内有氧训练"},
                {"name": "爬楼梯", "equipment": "无器械", "difficulty": "初级", "primary_muscles": ["心肺", "腿部"], "description": "日常有氧训练"}
            ],
            "intermediate": [
                {"name": "慢跑", "equipment": "无器械", "difficulty": "中级", "primary_muscles": ["心肺"], "description": "中等强度有氧"},
                {"name": "跳绳", "equipment": "跳绳", "difficulty": "中级", "primary_muscles": ["心肺", "小腿"], "description": "高效有氧训练"},
                {"name": "波比跳", "equipment": "无器械", "difficulty": "中级", "primary_muscles": ["全身", "心肺"], "description": "全身爆发力训练"}
            ]
        }
    }

def get_safety_guidelines():
    """
    获取安全训练指导原则
    
    Returns:
        dict: 包含各种安全指导原则
    """
    return {
        "general": [
            "训练前必须进行充分的热身运动",
            "训练后进行拉伸放松",
            "保持正确的动作姿态，宁轻勿重",
            "循序渐进增加训练强度",
            "保证充足的休息和睡眠",
            "如有任何不适立即停止训练"
        ],
        "beginner": [
            "初学者应从自重训练开始",
            "学会基础动作模式后再增加负重",
            "每次训练时间控制在30-45分钟",
            "一周训练3-4次，保证休息日",
            "重视动作质量胜过训练重量"
        ],
        "injury_prevention": [
            "有心血管疾病者必须咨询医生",
            "有关节问题者避免高冲击动作",
            "腰部有问题者避免重负荷脊柱训练",
            "膝盖有问题者减少深蹲类动作",
            "肩部有问题者避免过头推举动作",
            "任何急性疼痛应立即就医"
        ],
        "nutrition": [
            "训练前1-2小时适量进食",
            "训练后30分钟内补充蛋白质",
            "保证每日充足的水分摄入",
            "均衡饮食，避免过度节食",
            "减脂期控制热量摄入",
            "增肌期适当增加热量摄入"
        ]
    }

def get_exercises_by_goal_and_level(goal: str, level: str, target_areas: list = None):
    """
    根据目标和水平获取合适的训练动作
    
    Args:
        goal (str): 训练目标 ('weight_loss', 'muscle_gain', 'strength', 'endurance')
        level (str): 训练水平 ('beginner', 'intermediate', 'advanced')
        target_areas (list): 目标肌群列表
        
    Returns:
        dict: 推荐的训练动作
    """
    exercises = get_exercise_database()
    
    # 根据水平筛选难度
    difficulty_map = {
        'beginner': ['初级'],
        'intermediate': ['初级', '中级'],
        'advanced': ['初级', '中级', '高级']
    }
    
    suitable_difficulties = difficulty_map.get(level, ['初级'])
    
    # 根据目标调整训练重点
    goal_focus = {
        'weight_loss': ['cardio', 'legs', 'core'],  # 减脂重视有氧和大肌群
        'muscle_gain': ['chest', 'back', 'legs', 'shoulders', 'arms'],  # 增肌全面训练
        'strength': ['legs', 'back', 'chest'],  # 力量重视复合动作
        'endurance': ['cardio', 'core', 'legs'],  # 耐力重视心肺和核心
        'toning': ['core', 'legs', 'arms', 'shoulders']  # 塑形重视肌肉线条
    }
    
    # 如果指定了目标部位，使用目标部位；否则使用目标对应的重点部位
    if target_areas:
        focus_areas = [area.lower() for area in target_areas if area.lower() in exercises]
    else:
        focus_areas = goal_focus.get(goal, list(exercises.keys()))
    
    recommended_exercises = {}
    
    for area in focus_areas:
        if area in exercises:
            area_exercises = []
            for difficulty_level in ['beginner', 'intermediate']:
                if difficulty_level in exercises[area]:
                    for exercise in exercises[area][difficulty_level]:
                        if exercise['difficulty'] in suitable_difficulties:
                            area_exercises.append(exercise)
            recommended_exercises[area] = area_exercises
    
    return recommended_exercises

def get_disclaimer():
    """
    获取免责声明
    
    Returns:
        str: 免责声明文本
    """
    return """
⚠️ 重要免责声明：

1. 本应用提供的训练计划仅供参考，不能替代专业的健身指导和医疗建议。

2. 在开始任何训练计划前，建议咨询专业的健身教练或医生，特别是有健康问题或长期未运动者。

3. 训练过程中如出现任何不适、疼痛或异常症状，请立即停止训练并寻求专业医疗帮助。

4. 用户需根据自身实际情况调整训练强度和内容，循序渐进，量力而行。

5. 本应用不保存任何用户个人信息，所有数据仅在当前会话中使用。

6. 用户使用本应用产生的任何后果，开发者不承担责任。

请在充分理解以上声明的前提下使用本应用。安全永远是第一位的！
"""

if __name__ == "__main__":
    # 测试功能
    print("=== 健身知识库测试 ===")
    
    # 测试获取初学者减脂动作
    print("\n初学者减脂推荐动作：")
    exercises = get_exercises_by_goal_and_level('weight_loss', 'beginner')
    for area, exercise_list in exercises.items():
        print(f"\n{area.upper()}:")
        for exercise in exercise_list[:2]:  # 只显示前两个
            print(f"  - {exercise['name']}: {exercise['description']}")
    
    # 测试安全指导
    print("\n=== 安全指导原则 ===")
    guidelines = get_safety_guidelines()
    print("一般原则：")
    for guideline in guidelines['general'][:3]:
        print(f"  - {guideline}")
