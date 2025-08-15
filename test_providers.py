#!/usr/bin/env python3
"""
测试各个LLM Provider的行为
"""

import os
import sys
sys.path.append('.')

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def test_provider_clarity():
    """测试各个provider的调用逻辑是否清晰"""
    from utils.call_llm import call_llm
    
    print("🧪 测试LLM Provider逻辑清晰性")
    print("=" * 50)
    
    # 测试各个provider的调用方式
    providers_to_test = {
        "openai": "需要 OPENAI_API_KEY",
        "gemini": "需要 GEMINI_API_KEY (Google直接API)", 
        "deepseek": "需要 DEEPSEEK_API_KEY",
        "openrouter": "需要 OPENROUTER_API_KEY (推荐，统一API)"
    }
    
    for provider, description in providers_to_test.items():
        print(f"\n🔍 测试 {provider.upper()}")
        print(f"说明: {description}")
        
        # 检查必要的环境变量
        if provider == "openai":
            key_name = "OPENAI_API_KEY"
        elif provider == "gemini":
            key_name = "GEMINI_API_KEY"
        elif provider == "deepseek":
            key_name = "DEEPSEEK_API_KEY"
        elif provider == "openrouter":
            key_name = "OPENROUTER_API_KEY"
        
        api_key = os.getenv(key_name)
        if api_key and api_key != f"your-{provider}-api-key-here":
            try:
                # 只测试是否能正确设置，不实际调用
                print(f"✅ {key_name} 已配置")
                
                # 如果是当前配置的provider，实际测试一下
                current_provider = os.getenv("LLM_PROVIDER", "openai")
                if provider == current_provider:
                    print(f"🚀 当前使用的provider，测试调用...")
                    response = call_llm("简单回答：你好", provider=provider)
                    print(f"✅ 调用成功，响应长度: {len(response)}")
                    
            except Exception as e:
                print(f"❌ 测试失败: {e}")
        else:
            print(f"⚠️ {key_name} 未配置或使用模板值")
    
    print(f"\n📋 当前配置:")
    print(f"LLM_PROVIDER = {os.getenv('LLM_PROVIDER', 'openai')}")
    
    # 展示推荐配置
    print(f"\n💡 推荐配置 (最佳性能):")
    print(f"LLM_PROVIDER=openrouter")
    print(f"OPENROUTER_API_KEY=your-key")
    print(f"OPENROUTER_MODEL=google/gemini-2.5-flash")

def test_provider_differences():
    """说明各个provider的区别"""
    print(f"\n🔬 Provider 区别说明")
    print("=" * 50)
    
    differences = {
        "openai": {
            "调用方式": "OpenAI 官方API",
            "优势": "稳定可靠，GPT系列模型",
            "劣势": "相对较慢，费用较高",
            "使用场景": "需要最高质量输出时"
        },
        "gemini": {
            "调用方式": "Google 官方API",
            "优势": "免费额度大，速度快",
            "劣势": "API限制多，稳定性一般",
            "使用场景": "开发测试，简单任务"
        },
        "deepseek": {
            "调用方式": "DeepSeek 官方API",
            "优势": "便宜，中文友好",
            "劣势": "模型能力相对有限",
            "使用场景": "成本敏感的应用"
        },
        "openrouter": {
            "调用方式": "统一代理API",
            "优势": "支持多种模型，稳定可靠，可选择最优模型",
            "劣势": "需要额外注册",
            "使用场景": "生产环境推荐 (当前项目使用)"
        }
    }
    
    for provider, info in differences.items():
        print(f"\n📌 {provider.upper()}")
        for key, value in info.items():
            print(f"  {key}: {value}")

if __name__ == "__main__":
    test_provider_clarity()
    test_provider_differences()
    
    print(f"\n🎯 总结:")
    print(f"- openai/gemini/deepseek: 各自的直接API")  
    print(f"- openrouter: 统一代理API，可调用包括Gemini在内的多种模型")
    print(f"- 当前项目配置使用openrouter调用gemini-2.5-flash，获得最佳性能")
