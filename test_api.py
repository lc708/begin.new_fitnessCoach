#!/usr/bin/env python3
"""
测试API脚本 - 直接测试训练计划生成API，验证用户选择的时间安排是否被正确处理
"""

import requests
import json
import logging

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_plan_generation():
    """测试训练计划生成API"""
    
    # 测试数据：模拟用户选择每周6天、每次120分钟
    test_data = {
        "basic_info": {
            "age": 25,
            "gender": "男",
            "height": 175,
            "weight": 70,
            "experience": "intermediate"
        },
        "goals": {
            "primary_goal": "muscle_gain",
            "target_areas": ["全身"],
            "timeline": "8周"
        },
        "schedule": {
            "days_per_week": 6,  # 用户选择每周6天
            "time_per_session": 120  # 用户选择每次120分钟
        },
        "limitations": {
            "injuries": [],
            "restrictions": []
        }
    }
    
    print("🔍 测试数据:")
    print(f"用户选择: 每周{test_data['schedule']['days_per_week']}天，每次{test_data['schedule']['time_per_session']}分钟")
    print("=" * 60)
    
    try:
        # 调用API
        response = requests.post(
            'http://localhost:8000/api/generate-plan',
            json=test_data,
            headers={'Content-Type': 'application/json'},
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            
            if result.get('success'):
                plan = result['data']['plan']
                print("✅ API调用成功!")
                
                # 检查返回的计划是否包含用户选择的时间安排
                if 'overview' in plan:
                    print(f"📋 计划概述:")
                    print(f"  - 标题: {plan['overview'].get('title', 'N/A')}")
                    print(f"  - 频率: {plan['overview'].get('frequency', 'N/A')}")
                    print(f"  - 时长: {plan['overview'].get('session_time', 'N/A')}")
                
                # 检查每日计划的时长
                if 'daily_plans' in plan and plan['daily_plans']:
                    print(f"📅 每日计划检查:")
                    for i, day_plan in enumerate(plan['daily_plans']):
                        total_time = day_plan.get('total_time', 'N/A')
                        print(f"  - 第{i+1}天: {day_plan.get('day', 'N/A')} - {total_time}分钟")
                
                # 保存结果到文件以便进一步检查
                with open('test_result.json', 'w', encoding='utf-8') as f:
                    json.dump(result, f, ensure_ascii=False, indent=2)
                print("📄 详细结果已保存到 test_result.json")
                
            else:
                print(f"❌ API返回错误: {result.get('error', '未知错误')}")
                
        else:
            print(f"❌ HTTP错误: {response.status_code}")
            print(f"响应内容: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络错误: {e}")
        print("请确保后端服务正在运行 (python3 api.py)")
    except Exception as e:
        print(f"❌ 未知错误: {e}")

if __name__ == "__main__":
    test_plan_generation()
