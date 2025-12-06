from LLM.interface import LLMInterface
from LLM.LLMConfig import get_LLMConfig
from groq import AsyncGroq


class GroqProvider(LLMInterface):

    def __init__(self, api_key: str):
        self.client = AsyncGroq(api_key=get_LLMConfig().groq_api_key)
        self.model = get_LLMConfig().model
    
    async def generate_response(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
