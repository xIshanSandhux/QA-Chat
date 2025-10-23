import uuid

async def session_id_gen():
    return str(uuid.uuid4())

# print(str(uuid.uuid4()))