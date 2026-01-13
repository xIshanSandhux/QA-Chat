from abc import ABC, abstractmethod
from typing import List
class LLMInterface(ABC):

    @abstractmethod
    async def generate_response(self, prompt: str, history: List[dict[str,str]]) -> str:
        pass

    @abstractmethod
    async def query_rewrite(self, query: str) -> str:
        pass

    def stream_response(self, prompt: str):
        raise NotImplementedError("Stream response is not implemented")