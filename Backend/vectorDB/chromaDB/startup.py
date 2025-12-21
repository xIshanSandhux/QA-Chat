# initialization for chromaDB

import chromadb 

client = None  
collection = None


async def start_chromadb():
    global client 
    global collection
    client  = await chromadb.AsyncHttpClient(host='localhost', port=8001)
    heartbeat =await client.heartbeat()

    if not heartbeat:
        raise Exception("Failed to connect to chromaDB")
    collection = await client.get_or_create_collection(name='mvp_collection', embedding_function=None)

async def get_chromadb_client():
    global client
    if not client:
        raise Exception("ChromaDB not connected")
    return client

def get_collection():
    global collection
    if not collection:
        raise Exception("Collection not created")
    return collection

async def shutdown_chromadb():
    global client
    global collection
    await client.delete_collection(name='mvp_collection')
    print("ChromaDB shut down successfully (deleted collection)")