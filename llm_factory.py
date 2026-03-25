import os

LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "ollama")

LLM_CONFIGS = {
    "ollama": {
        "provider": "openai",
        "model": "llama3.1",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
    },
    "openai": {
        "provider": "openai",
        "model": "gpt-4.1",
    },
    "gemini": {
        "provider": "google_genai",
        "model": "gemini-2.5-flash",
    },
}


def create_llm(provider: str = LLM_PROVIDER):
    config = {**LLM_CONFIGS[provider]}
    provider_type = config.pop("provider")

    if provider_type == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(**config)
    elif provider_type == "google_genai":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(**config)
    else:
        raise ValueError(f"Unknown provider type: {provider_type}")
