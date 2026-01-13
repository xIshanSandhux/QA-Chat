from abc import ABC, abstractmethod

class chatHistoryInterface(ABC):
    @abstractmethod
    async def addChat(self, session_id: str, role: str, query: str):
       pass

    @abstractmethod
    async def getChatHistory(self, session_id: str):
        pass
 