import redis
import json
from api.redis.initialization import get_redis, set_redis
from fastapi import HTTPException, status

# session_id = "session_id"
#     chat_history = [
#     {"role": "user", "message": "Hello"},
#     {"role": "assistant", "message": "Hi there!"}
#     ]
#     chat_redis.set(session_id, json.dumps(chat_history))
#     print(chat_redis.get(session_id))

# example of full chat
# fullChatexample = [
#     {"role": "user", "parts": [{"text": "Explain how AI works in a few words"}]}, 
# {"role": "model", "parts": [{"text": "AI is a technology that allows machines to learn and make decisions based on data."}]},
# ]

# adding to chat history
async def addToChat(session_id: str, role: str, text: str):
    try:
        chat_history = await get_redis(session_id)
        current_chat = {"role": role, "parts": [{"text": text}]}
        if chat_history is None:
            await set_redis(session_id, json.dumps([current_chat]))
        else:
            chat_history = json.loads(chat_history)
            chat_history.append(current_chat)
            await set_redis(session_id, json.dumps(chat_history))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

async def getChatHistory(session_id: str):
    chat_history = await get_redis(session_id)
    if chat_history is None:
        return []
    return json.loads(chat_history)

# async def getChatLength(session_id: str) -> int:


