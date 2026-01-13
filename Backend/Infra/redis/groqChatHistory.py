from math import exp
from .chatHistoryInterface import chatHistoryInterface
from .initialization import setRedisChatList,getFullChat, getChatLen
import json
class groqChat(chatHistoryInterface):

    async def addChat(self, session_id: str, role: str, query: str):
        try:
            current = {"role": role,"content":query}
            await setRedisChatList(session_id,json.dumps(current))
        except Exception as e:
            raise Exception(str(e))
        
    async def getChatHistory(self, session_id: str):
            try:
                chat = await getFullChat(session_id)
                if chat is None:
                    raise
                fullchat = [json.loads(x) for x in chat]
                return fullchat
            except Exception as e:
                raise Exception(str(e))
    
    async def getChatLength(self, session_id: str):
        try:
            length = await getChatLen(session_id)
            return length
        except Exception as e:
            print("Error getting the chat length")
            print(f"Error: {str(e)}")