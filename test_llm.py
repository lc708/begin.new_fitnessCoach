#!/usr/bin/env python3
"""
测试LLM调用 - 验证LLM服务是否正常工作
"""

import sys
import os
sys.path.append('.')

from utils.call_llm import call_llm, call_llm_with_system

def test_llm_connection():
    """测试各个LLM提供商的连接"""
    
    providers = ["openai", "gemini", "deepseek"]
    
    for provider in providers:
        print(f"\n🔍 测试 {provider.upper()}:")
        print("=" * 40)
        
        try:
            # 设置环境变量（假设正在使用这个提供商）
            os.environ["LLM_PROVIDER"] = provider
            
            # 简单测试
            response = call_llm("请回答：你好")
            print(f"✅ {provider} 连接正常")
            print(f"响应: {response[:100]}...")
            
            # 测试system prompt
            system_response = call_llm_with_system(
                "你是一个健身教练", 
                "请为初学者推荐一个简单的训练计划"
            )
            print(f"✅ {provider} system prompt 正常")
            print(f"系统响应: {system_response[:100]}...")
            
            break  # 找到可用的提供商就停止
            
        except Exception as e:
            print(f"❌ {provider} 连接失败: {e}")
            continue
    
    else:
        print("\n❌ 所有LLM提供商都无法连接!")
        print("请检查:")
        print("1. 环境变量配置 (OPENAI_API_KEY, GEMINI_API_KEY, DEEPSEEK_API_KEY)")
        print("2. 网络连接")
        print("3. API配额")

def test_training_prompt():
    """测试训练计划生成的提示词"""
    
    print("\n🏋️ 测试训练计划生成提示词:")
    print("=" * 50)
    
    system_prompt = """你是一位资深的健身教练，请根据用户的分析结果和可用的训练动作，生成一份详细的个性化训练计划。

**核心原则：严格遵守用户指定的训练频率和时长，绝对不能随意更改！**

计划必须包含：
1. 训练概述和原则（强调按照用户要求的频率和时长）
2. 具体的周训练安排（必须严格按照用户要求的天数）
3. 每日训练内容（每次训练必须符合用户指定的时长）
4. 动作要点和注意事项
5. 进阶建议

重要提醒：
- 如果用户要求每周2次，就只能安排2次，不能是3次或其他
- 如果用户要求每次45分钟，每次训练的总时长必须是45分钟，不能是10分钟或其他时长
- 根据用户的时间安排合理分配动作数量和组数

请以结构化的方式返回，内容要专业且易于理解。"""

    user_prompt = """
**重要要求：请严格按照用户的时间安排生成计划**

用户明确要求：
- 训练频率：每周必须是6次（不能多也不能少）
- 每次时长：每次必须是120分钟（不能随意改变）

用户详细数据：
- 主要目标：muscle_gain
- 训练水平：intermediate
- 严格训练频率：每周6次
- 严格训练时长：每次120分钟
- 身体限制：无

**请务必严格遵守用户的时间安排，生成一份每周6次、每次120分钟的完整训练计划。**
"""
    
    try:
        response = call_llm_with_system(system_prompt, user_prompt)
        print("✅ 训练计划生成成功!")
        print(f"响应内容: {response[:500]}...")
        
        # 检查响应中是否包含用户要求的时间安排
        if "6次" in response and "120" in response:
            print("✅ 响应中包含用户要求的时间安排!")
        else:
            print("⚠️ 响应中可能没有正确反映用户的时间安排")
            
    except Exception as e:
        print(f"❌ 训练计划生成失败: {e}")

if __name__ == "__main__":
    test_llm_connection()
    test_training_prompt()
