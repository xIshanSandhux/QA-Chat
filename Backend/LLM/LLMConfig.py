from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class LLMConfig(BaseSettings):
    model: str = 'llama-3.1-8b-instant'
    groq_api_key: str = ''
    google_api_key: str = ''
    open_router_api_key: str = ''
    provider: str = 'groq'

    model_config = SettingsConfigDict(env_file='.env')
    

@lru_cache
def get_LLMConfig():
    return LLMConfig()