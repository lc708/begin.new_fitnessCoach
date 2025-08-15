from flow import create_fitness_plan_flow
import json
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    """主函数 - 演示健身计划生成流程"""
    
    # 示例用户数据
    sample_user_data = {
        "basic_info": {
            "age": 25,
            "gender": "男",
            "height": 175,
            "weight": 70,
            "experience": "beginner"
        },
        "goals": {
            "primary_goal": "muscle_gain",
            "target_areas": ["chest", "arms"],
            "timeline": "4周"
        },
        "schedule": {
            "days_per_week": 3,
            "time_per_session": 45
        },
        "limitations": {
            "injuries": [],
            "restrictions": []
        }
    }
    
    # 初始化共享存储
    shared = {
        "user_data": sample_user_data,
        # 其他字段将在流程中填充
        "validation_errors": [],
        "data_is_valid": False,
        "analysis_result": {},
        "raw_plan": {},
        "final_plan": {},
        "generation_completed": False
    }
    
    print("🏋️ FitCoach 个性化健身计划生成系统")
    print("=" * 50)
    print("正在为您生成个性化训练计划...")
    print()
    
    try:
        # 创建并运行健身计划生成流程
        fitness_flow = create_fitness_plan_flow()
        fitness_flow.run(shared)
        
        # 检查是否生成成功
        if shared.get('generation_completed', False):
            final_plan = shared.get('final_plan', {})
            formatted_plan = final_plan.get('formatted_plan', {})
            
            print("✅ 训练计划生成完成！")
            print()
            
            # 显示计划概述
            overview = formatted_plan.get('overview', {})
            print(f"📋 {overview.get('title', '个性化训练计划')}")
            print(f"📅 创建时间: {overview.get('created_date', '')}")
            print(f"⏱️ 训练频率: {overview.get('frequency', '')}")
            print(f"🕐 每次时长: {overview.get('session_time', '')}")
            print()
            
            # 显示用户档案
            user_profile = formatted_plan.get('user_profile', {})
            if user_profile:
                print("👤 用户档案:")
                for key, value in user_profile.items():
                    print(f"   {key}: {value}")
                print()
            
            # 显示周训练安排
            weekly_schedule = formatted_plan.get('weekly_schedule', {})
            if weekly_schedule:
                print("📅 周训练安排:")
                for day, content in weekly_schedule.items():
                    print(f"   {day}: {content}")
                print()
            
            # 显示每日计划摘要
            daily_plans = formatted_plan.get('daily_plans', [])
            if daily_plans:
                print(f"📋 详细训练计划 (共{len(daily_plans)}天):")
                for i, plan in enumerate(daily_plans[:3], 1):  # 只显示前3天
                    print(f"   第{i}天 - {plan.get('focus', '')}: {len(plan.get('main_workout', []))}个动作")
                if len(daily_plans) > 3:
                    print(f"   ... 还有{len(daily_plans)-3}天的计划")
                print()
            
            # 显示安全提醒
            safety_notes = formatted_plan.get('safety_notes', [])
            if safety_notes:
                print("⚠️ 安全提醒:")
                for note in safety_notes[:3]:  # 只显示前3条
                    print(f"   {note}")
                if len(safety_notes) > 3:
                    print(f"   ... 还有{len(safety_notes)-3}条安全提醒")
                print()
            
            # 显示使用提示
            tips = formatted_plan.get('tips', [])
            if tips:
                print("💡 使用提示:")
                for tip in tips:
                    print(f"   {tip}")
                print()
            
            print("=" * 50)
            print("🎉 完整的训练计划已生成！")
            print("💾 请截图保存此计划，系统不会保存您的个人信息。")
            print("🔄 如需调整计划，请重新填写数据生成。")
            
        else:
            print("❌ 训练计划生成失败")
            if shared.get('validation_errors'):
                print("验证错误:", shared['validation_errors'])
                
    except Exception as e:
        print(f"❌ 系统错误: {e}")
        logging.error(f"主流程执行失败: {e}")

def test_with_custom_data():
    """使用自定义数据测试"""
    print("请输入您的基本信息：")
    
    try:
        age = int(input("年龄: "))
        gender = input("性别 (男/女): ").strip()
        height = float(input("身高 (cm): "))
        weight = float(input("体重 (kg): "))
        
        print("\n健身经验：")
        print("1. beginner (初学者)")
        print("2. intermediate (有经验)")  
        print("3. advanced (高级)")
        exp_choice = input("请选择 (1-3): ").strip()
        experience_map = {'1': 'beginner', '2': 'intermediate', '3': 'advanced'}
        experience = experience_map.get(exp_choice, 'beginner')
        
        print("\n主要目标：")
        print("1. weight_loss (减脂)")
        print("2. muscle_gain (增肌)")
        print("3. strength (力量)")
        print("4. toning (塑形)")
        goal_choice = input("请选择 (1-4): ").strip()
        goal_map = {'1': 'weight_loss', '2': 'muscle_gain', '3': 'strength', '4': 'toning'}
        primary_goal = goal_map.get(goal_choice, 'toning')
        
        days_per_week = int(input("每周训练天数 (2-6): "))
        time_per_session = int(input("每次训练时长 (分钟): "))
        
        # 构建用户数据
        custom_user_data = {
            "basic_info": {
                "age": age,
                "gender": gender,
                "height": height,
                "weight": weight,
                "experience": experience
            },
            "goals": {
                "primary_goal": primary_goal,
                "target_areas": ["全身"],
                "timeline": "4周"
            },
            "schedule": {
                "days_per_week": days_per_week,
                "time_per_session": time_per_session
            },
            "limitations": {
                "injuries": [],
                "restrictions": []
            }
        }
        
        # 运行生成流程
        shared = {
            "user_data": custom_user_data,
            "validation_errors": [],
            "data_is_valid": False,
            "analysis_result": {},
            "raw_plan": {},
            "final_plan": {},
            "generation_completed": False
        }
        
        print("\n正在生成您的个性化训练计划...")
        fitness_flow = create_fitness_plan_flow()
        fitness_flow.run(shared)
        
        # 输出结果（简化版）
        if shared.get('generation_completed', False):
            print("\n✅ 您的个性化训练计划已生成！")
            final_plan = shared['final_plan']['formatted_plan']
            overview = final_plan.get('overview', {})
            print(f"📋 {overview.get('title', '')}")
            print(f"⏱️ {overview.get('frequency', '')} | {overview.get('session_time', '')}")
        else:
            print("\n❌ 计划生成失败，请检查输入数据")
            
    except KeyboardInterrupt:
        print("\n\n用户取消操作")
    except Exception as e:
        print(f"\n❌ 输入错误: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--custom":
        test_with_custom_data()
    else:
        main()