#!/usr/bin/env python3
"""
测试OPENROUTER GEMINI配置
"""

import os
import sys
sys.path.append('.')

# 加载.env文件
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ 已加载.env文件")
except ImportError:
    print("⚠️ 没有安装python-dotenv，请手动设置环境变量")
except Exception as e:
    print(f"⚠️ 加载.env文件失败: {e}")

def test_openrouter_gemini():
    """测试通过OPENROUTER调用GEMINI"""
    
    # 设置环境变量
    os.environ["LLM_PROVIDER"] = "openrouter"
    
    # 检查必要的环境变量
    if not os.getenv("OPENROUTER_API_KEY"):
        print("❌ 请设置 OPENROUTER_API_KEY 环境变量")
        print("获取API Key: https://openrouter.ai/keys")
        return False
    
    print("🔍 测试OPENROUTER GEMINI配置")
    print("=" * 40)
    
    try:
        from utils.call_llm import call_llm_with_system
        
        # 测试简单调用
        system_prompt = "你是一个专业的健身教练。"
        user_prompt = "为一个25岁男性，每周训练3次，每次45分钟，制定一个简单的增肌计划大纲。"
        
        print("🚀 发送请求到GEMINI 2.0 Flash...")
        print(f"系统提示: {system_prompt}")
        print(f"用户请求: {user_prompt}")
        print("-" * 40)
        
        response = call_llm_with_system(system_prompt, user_prompt)
        
        print("✅ 成功收到响应!")
        print(f"响应长度: {len(response)} 字符")
        print(f"响应预览: {response[:200]}...")
        
        # 检查响应质量
        if "3次" in response and ("45" in response or "45分钟" in response):
            print("✅ 响应包含用户要求的训练频率和时长!")
        else:
            print("⚠️ 响应可能没有完全遵循用户要求")
        
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        print("\n可能的问题:")
        print("1. OPENROUTER_API_KEY 未设置或无效")
        print("2. 网络连接问题")
        print("3. API配额不足")
        return False

def test_speed():
    """测试响应速度"""
    import time
    
    print("\n🚀 测试响应速度...")
    print("=" * 40)
    
    try:
        from utils.call_llm import call_llm
        
        start_time = time.time()
        response = call_llm("简单回答：健身最重要的是什么？")
        end_time = time.time()
        
        response_time = end_time - start_time
        print(f"✅ 响应时间: {response_time:.2f} 秒")
        print(f"响应: {response}")
        
        if response_time < 10:
            print("✅ 响应速度良好!")
        elif response_time < 30:
            print("⚠️ 响应速度一般，可以接受")
        else:
            print("❌ 响应速度较慢")
            
    except Exception as e:
        print(f"❌ 速度测试失败: {e}")

if __name__ == "__main__":
    print("🏋️ FitCoach OPENROUTER GEMINI 测试")
    print("=" * 50)
    
    success = test_openrouter_gemini()
    
    if success:
        test_speed()
        print("\n🎉 OPENROUTER GEMINI 配置测试完成!")
        print("现在可以使用训练计划生成功能了。")
    else:
        print("\n❌ 配置测试失败，请检查环境变量设置。")
