import redis.asyncio as redis
from fastapi import HTTPException
import asyncio
chat_redis = None

def start_redis():
    global chat_redis
    try:
        chat_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
        if not chat_redis.ping():
            raise redis.ConnectionError    
    except redis.ConnectionError:
        raise HTTPException(status_code=500, detail="Failed to connect to Redis")
    except redis.ResponseError:
        print("Please check the command, it appears to be wrong")
    print("Redis connected successfully")

async def shutdown_redis():
    global chat_redis
    if not chat_redis:
        return
    try:
        await chat_redis.close()
    except redis.ConnectionError:
        print("Failed to shutdown Redis due to connection issues")
    except redis.TimeoutError:
        print("Redis was taking too long to shutdown")
    except redis.ResponseError:
        print("Please check the command, it appears to be wrong")
    print("Redis shut down successfully")

async def get_redis(session_id: str):
    global chat_redis
    try:
        if not chat_redis:
            raise redis.ConnectionError
        return await chat_redis.get(session_id)
    except redis.ConnectionError:
        print("Missing redis client while running the get command")
    except redis.ResponseError:
        print("Please check the get command syntax and argument")

async def set_redis(session_id: str, query: str):
    global chat_redis
    try:
        if not chat_redis:
            raise redis.ConnectionError
        await chat_redis.set(session_id, query)
    except redis.ConnectionError:
        print("Missing redis client while running the set command")
    except redis.ResponseError:
        print("Please check the set command syntax and argument") 
   
async def getChatLen(session_id: str)-> int |None:
    global chat_redis
    try:
        if not chat_redis:
            raise redis.ConnectionError
        return await chat_redis.llen(session_id)
    except redis.ConnectionError:
        print("Check Redis client, not able to get the client for chat length")

async def setRedisChatList(session_id: str, query: str) -> None:
    global chat_redis
    try:
        if not chat_redis:
            raise redis.ConnectionError
        chatLen = await getChatLen(session_id)
        add = chat_redis.rpush(session_id,query)
        if chatLen == add:
            raise redis.ResponseError
    except redis.ConnectionError:
        print("Missing redis client while running the set command")
    except redis.ResponseError:
        print("Please check the list push command syntax and argument") 

async def getFullChat(session_id: str):
    global chat_redis

    try:
        if not chat_redis:
            raise redis.ConnectionError
        
        history = await chat_redis.lrange(session_id,0,-1)
        if len(history)==0:
            raise redis.ResponseError
        return history
    except redis.ResponseError:
        print("please check the command and the chat not able to get full chat history")
    except redis.ConnectionError:
        print("Unable to process the chat history command due to connection Error")

    
        
 
