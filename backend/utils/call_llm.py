import os
from typing import Optional
import dotenv

dotenv.load_dotenv()

def call_llm(prompt: str, provider: Optional[str] = None) -> str:
    """
    Call LLM with support for multiple providers.
    
    Args:
        prompt: The prompt to send to the LLM
        provider: LLM provider to use. If None, uses LLM_PROVIDER env var.
                 Supported providers:
                 - openai: OpenAI GPT models (直接API)
                 - gemini: Google Gemini models (直接API，需要GEMINI_API_KEY)  
                 - deepseek: DeepSeek models (直接API)
                 - openrouter: 通过OpenRouter调用各种模型 (统一API，推荐用于Gemini)
    
    Returns:
        The LLM response as a string
    """
    # Determine provider
    if provider is None:
        provider = os.getenv("LLM_PROVIDER", "openai").lower()
    
    if provider == "openai":
        from openai import OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        client = OpenAI(api_key=api_key)
        model = os.getenv("OPENAI_MODEL", "gpt-5-mini")
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    elif provider == "gemini":
        try:
            import google.generativeai as genai
        except ImportError:
            raise ImportError("Please install google-generativeai: pip install google-generativeai")
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-2.5-flash"))
        response = model.generate_content(prompt)
        return response.text
    
    elif provider == "deepseek":
        from openai import OpenAI
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found in environment variables")
        
        # DeepSeek uses OpenAI-compatible API
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1"
        )
        model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    elif provider == "openrouter":
        # 通用OPENROUTER接口 - call_llm版本
        from openai import OpenAI
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
        
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
        model = os.getenv("OPENROUTER_MODEL", "google/gemini-2.5-flash")
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            timeout=60.0
        )
        return response.choices[0].message.content
    
    else:
        raise ValueError(f"Unsupported provider: {provider}. Choose from: openai, gemini, deepseek, openrouter")

def call_llm_with_system(system_prompt: str, user_prompt: str, provider: Optional[str] = None) -> str:
    """
    Call LLM with system and user prompts.
    
    Args:
        system_prompt: The system prompt to set context
        user_prompt: The user prompt
        provider: LLM provider to use. Supported providers:
                 - openai: OpenAI GPT models (直接API)
                 - gemini: Google Gemini models (直接API，system+user会合并)
                 - deepseek: DeepSeek models (直接API)
                 - openrouter: 通过OpenRouter调用各种模型 (统一API，当前推荐)
    
    Returns:
        The LLM response as a string
    """
    # Determine provider
    if provider is None:
        provider = os.getenv("LLM_PROVIDER", "openai").lower()
    
    if provider == "openai":
        from openai import OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        client = OpenAI(api_key=api_key)
        model = os.getenv("OPENAI_MODEL", "gpt-5-mini")
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
    
    elif provider == "gemini":
        # 使用Google官方API直接调用GEMINI
        try:
            import google.generativeai as genai
        except ImportError:
            raise ImportError("Please install google-generativeai: pip install google-generativeai")
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-2.5-flash"))
        
        # 对于Google直接API，需要合并system和user prompts
        combined_prompt = f"System: {system_prompt}\n\nUser: {user_prompt}"
        response = model.generate_content(combined_prompt)
        return response.text
    
    elif provider == "deepseek":
        from openai import OpenAI
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found in environment variables")
        
        # DeepSeek uses OpenAI-compatible API
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1"
        )
        model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
    
    elif provider == "openrouter":
        # 通用OPENROUTER接口 - call_llm_with_system版本
        from openai import OpenAI
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
        
        client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
        model = os.getenv("OPENROUTER_MODEL", "google/gemini-2.5-flash")
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            timeout=60.0
        )
        return response.choices[0].message.content
    
    else:
        raise ValueError(f"Unsupported provider: {provider}. Choose from: openai, gemini, deepseek, openrouter")

if __name__ == "__main__":
    # Test with different providers
    test_prompt = "Hello, how are you? Please respond in one sentence."
    
    print("Testing LLM providers...")
    print("-" * 50)
    
    # Test current provider
    try:
        current_provider = os.getenv("LLM_PROVIDER", "openai")
        print(f"Current provider ({current_provider}):")
        response = call_llm(test_prompt)
        print(f"Response: {response}")
        print("-" * 50)
        
        # Test system + user prompt
        print("Testing system + user prompts:")
        system_prompt = "You are a helpful fitness assistant."
        user_prompt = "What is the most important thing for beginners?"
        response2 = call_llm_with_system(system_prompt, user_prompt)
        print(f"Response: {response2}")
        print("-" * 50)
        
    except Exception as e:
        print(f"Error: {e}")
        print("-" * 50)
