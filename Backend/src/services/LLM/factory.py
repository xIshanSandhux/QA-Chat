from .LLMConfig import get_LLMConfig
from .Providers.groqProvider import GroqProvider
from functools import lru_cache


def getLLMProvider():
    provider = get_LLMConfig().provider

    match provider:
        case 'groq':
            print('groq provider')
            return GroqProvider(get_LLMConfig().groq_api_key, get_LLMConfig().model)
        case _:
            raise ValueError(f"Provider {provider} not supported")

@lru_cache
def LLMProviderFactory():
    return getLLMProvider()