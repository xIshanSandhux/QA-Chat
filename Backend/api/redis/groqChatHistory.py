from math import exp
from .chatHistoryInterface import chatHistoryInterface
from .initialization import get_redis, set_redis
import json
class groqChat(chatHistoryInterface):

    async def addChat(session_id: str, role: str, query: str):
        try:
            chat_hist = await get_redis(session_id)
            current = {"role": role,"content":query}
            # need to check how to store as a list instead of 
            # converting to a string because current I am converting
            # it back to list and then updating which is slow
            if chat_hist is None:
                await set_redis(session_id,json.dumps([current]))
        except Exception as e:
            raise Exception(str(e))