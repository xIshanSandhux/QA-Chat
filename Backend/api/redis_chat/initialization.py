import redis 
from fastapi import HTTPException

chat_redis = None

async def start_redis():
    global chat_redis
    chat_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
    if not chat_redis.ping():
        raise HTTPException(status_code=500, detail="Failed to connect to Redis")
    print("Redis connected successfully")

async def shutdown_redis():
    global chat_redis
    chat_redis.close()
   




# redis_client.set('foo', 'bar')
# # True
# print(redis_client.get('foo'))
# # bar

# r.hset('user-session:123', mapping={
#     'name': 'John',
#     "surname": 'Smith',
#     "company": 'Redis',
#     "age": 29
# })  
# # True

# r.hgetall('user-session:123')
# # {'surname': 'Smith', 'name': 'John', 'company': 'Redis', 'age': '29'}

