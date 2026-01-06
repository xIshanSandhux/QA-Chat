from math import exp
from .chatHistoryInterface import chatHistoryInterface
from .initialization import setRedisChatList
import json
class groqChat(chatHistoryInterface):

    async def addChat(self, session_id: str, role: str, query: str):
        try:
            current = {"role": role,"content":query}
            await setRedisChatList(session_id,json.dumps(current))
        except Exception as e:
            raise Exception(str(e))