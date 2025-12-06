from ..interface import LLMInterface
from groq import AsyncGroq


class GroqProvider(LLMInterface):

    def __init__(self, key: str, model: str):
        self.client = AsyncGroq(api_key=key)
        self.model = model

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
