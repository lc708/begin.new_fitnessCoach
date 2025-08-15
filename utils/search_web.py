import os
import requests
from typing import List, Dict, Optional
from duckduckgo_search import DDGS

def search_web(query: str, provider: Optional[str] = None, num_results: int = 5) -> str:
    """
    Search the web using various providers.
    
    Args:
        query: Search query
        provider: Search provider to use ('serper', 'tavily', 'brave', 'bocha', 'duckduckgo'). 
                 If None, uses SEARCH_PROVIDER env var or defaults to 'duckduckgo'
        num_results: Number of results to return
    
    Returns:
        Formatted search results as string
    """
    # Determine provider
    if provider is None:
        provider = os.getenv("SEARCH_PROVIDER", "duckduckgo").lower()
    
    if provider == "serper":
        return search_serper(query, num_results)
    elif provider == "tavily":
        return search_tavily(query, num_results)
    elif provider == "brave":
        return search_brave(query, num_results)
    elif provider == "bocha":
        return search_bocha(query, num_results)
    elif provider == "duckduckgo":
        return search_duckduckgo(query, num_results)
    else:
        raise ValueError(f"Unsupported provider: {provider}. Choose from: serper, tavily, brave, bocha, duckduckgo")

def search_serper(query: str, num_results: int = 5) -> str:
    """Search using Serper API"""
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError("SERPER_API_KEY not found in environment variables")
    
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "q": query,
        "num": num_results
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for item in data.get("organic", [])[:num_results]:
            results.append(f"Title: {item.get('title', '')}\nURL: {item.get('link', '')}\nSnippet: {item.get('snippet', '')}")
        
        return "\n\n".join(results) if results else "No results found"
    except Exception as e:
        return f"Serper search error: {str(e)}"

def search_tavily(query: str, num_results: int = 5) -> str:
    """Search using Tavily API"""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY not found in environment variables")
    
    url = "https://api.tavily.com/search"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "api_key": api_key,
        "query": query,
        "max_results": num_results,
        "search_depth": "basic"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for item in data.get("results", [])[:num_results]:
            results.append(f"Title: {item.get('title', '')}\nURL: {item.get('url', '')}\nSnippet: {item.get('content', '')}")
        
        return "\n\n".join(results) if results else "No results found"
    except Exception as e:
        return f"Tavily search error: {str(e)}"

def search_brave(query: str, num_results: int = 5) -> str:
    """Search using Brave Search API"""
    api_key = os.getenv("BRAVE_API_KEY")
    if not api_key:
        raise ValueError("BRAVE_API_KEY not found in environment variables")
    
    url = f"https://api.search.brave.com/res/v1/web/search?q={query}&count={num_results}"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for item in data.get("web", {}).get("results", [])[:num_results]:
            results.append(f"Title: {item.get('title', '')}\nURL: {item.get('url', '')}\nSnippet: {item.get('description', '')}")
        
        return "\n\n".join(results) if results else "No results found"
    except Exception as e:
        return f"Brave search error: {str(e)}"

def search_bocha(query: str, num_results: int = 5) -> str:
    """Search using Bocha API (bochaai.com)"""
    api_key = os.getenv("BOCHA_API_KEY")
    if not api_key:
        raise ValueError("BOCHA_API_KEY not found in environment variables")
    
    url = "https://api.bochaai.com/v1/web-search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": query,
        "summary": True,
        "count": num_results
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        results = []
        # Process web search results
        for item in data.get("results", [])[:num_results]:
            results.append(f"Title: {item.get('title', '')}\nURL: {item.get('url', '')}\nSnippet: {item.get('snippet', '')}")
        
        # Add summary if available
        if data.get("summary"):
            results.insert(0, f"Summary: {data['summary']}\n")
        
        return "\n\n".join(results) if results else "No results found"
    except Exception as e:
        return f"Bocha search error: {str(e)}"

def search_duckduckgo(query: str, num_results: int = 5) -> str:
    """Search using DuckDuckGo (no API key required)"""
    try:
        results_list = DDGS().text(query, max_results=num_results)
        
        results = []
        for item in results_list:
            results.append(f"Title: {item.get('title', '')}\nURL: {item.get('href', '')}\nSnippet: {item.get('body', '')}")
        
        return "\n\n".join(results) if results else "No results found"
    except Exception as e:
        return f"DuckDuckGo search error: {str(e)}"

if __name__ == "__main__":
    # Test search functionality
    test_query = "What is MetaAgentCore MACore?"
    
    print("Testing search providers...")
    print("-" * 50)
    
    # Test current provider
    try:
        current_provider = os.getenv("SEARCH_PROVIDER", "duckduckgo")
        print(f"Current provider ({current_provider}):")
        results = search_web(test_query)
        print(results)
        print("-" * 50)
    except Exception as e:
        print(f"Error: {e}")
        print("-" * 50)
