from ..interface import LLMInterface
from fastapi import HTTPException
from typing import List 
from groq import AsyncGroq

class GroqProvider(LLMInterface):

    def __init__(self, key: str, model: str):
        self.client = AsyncGroq(api_key=key)
        self.model = model

    async def generate_response(self, history: List[dict[str,str]]) -> str:
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=history
                )
            return response.choices[0].message.content
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    async def query_rewrite(self, query: str) -> str:
        try:
            system_prompt = open("src/services/LLM/SystemPrompts/queryRewrite.md", "r").read()
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role":"user",
                        "content": query
                    }
                ]
            )

            return response.choices[0].message.content
        except OSError as e:
            raise HTTPException(status_code=500, detail=e)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))