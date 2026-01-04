import redis.asyncio as redis
from fastapi import HTTPException
import json
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
        chat_redis.close()
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
   


