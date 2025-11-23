# chroma implementation for the vector database


from .startup import get_collection as collection
from embedding.embed import embedDoc
from typing import List
import uuid

def createID(length: int):
    if not length:
        raise ValueError("Length must be greater than 0")
    ids = [str(uuid.uuid4()) for _ in range(length)]
    return ids

def metadata(sessionId: str, length: int):
    sessionIds = [{"sessionId": sessionId} for _ in range(length)]
    return sessionIds


async def add_chunks(sessionId: str, chunks: List[str]):
    chunk_ids= createID(len(chunks))
    chunk_metadata = metadata(sessionId, len(chunks))
    chunk_embeddings = await embedDoc(chunks)
    await collection().add(
        ids=chunk_ids,
        embeddings=chunk_embeddings,
        documents=chunks,
        metadatas=chunk_metadata
    )
    return await collection().count()

async def getQueryChunks(sessionId: str, query: str):
    print("Getting query chunks")
    print("Session ID: ", sessionId)
    print("Query: ", query)
    queryEmbedding = await embedDoc([query])
    # print("Query embedding")
    # print(queryEmbedding)
    relChunks = await collection().query(
        query_embeddings=queryEmbedding,
        n_results=5,
        where={"sessionId": sessionId},
        include=["documents", "metadatas"]
    )
    print("--------------------------------REL CHUNKS--------------------------------")
    print(relChunks)
    # chunks = await collection().get(where={"sessionId": sessionId})
    print("--------------------------------REL CHUNKS--------------------------------")
    # print(ch/unks)
    return relChunks



    
