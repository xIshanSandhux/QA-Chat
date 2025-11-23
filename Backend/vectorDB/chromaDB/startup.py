# initialization for chromaDB

import chromadb 
import asyncio


client = None  


async def start_chromadb():
    global client 
    client  = await chromadb.AsyncHttpClient(host='localhost', port=8001)
    heartbeat =await client.heartbeat()

    if not heartbeat:
        raise Exception("Failed to connect to chromaDB")
    print("ChromaDB connected successfully")

async def get_chromadb_client():
    global client
    if not client:
        raise Exception("ChromaDB not connected")
    return client