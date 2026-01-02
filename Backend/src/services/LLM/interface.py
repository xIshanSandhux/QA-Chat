from abc import ABC, abstractmethod

class LLMInterface(ABC):

    @abstractmethod
    async def generate_response(self, prompt: str) -> str:
        pass

    @abstractmethod
    async def query_rewrite(self, query: str) -> str:
        pass

    def stream_response(self, prompt: str):
        raise NotImplementedError("Stream response is not implemented")