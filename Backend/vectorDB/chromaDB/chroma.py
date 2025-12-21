# chroma implementation for the vector database


from .startup import get_collection as collection
from RAG.embedding.embed import embedDoc
from typing import List
import uuid

def createID(length: int):
    if not length:
        raise ValueError("Length must be greater than 0")
    ids = [str(uuid.uuid4()) for _ in range(length)]
    return ids

def metadata(sessionId: str, length: int, pageNumber: int):
    chunkMetadata = [{"sessionId": sessionId,"pageNumber": pageNumber} for _ in range(length)]
    return chunkMetadata


async def add_chunks(sessionId: str, chunks: List[str], pageNumber: int):
    chunk_ids= createID(len(chunks))
    chunk_metadata = metadata(sessionId, len(chunks),pageNumber)
    chunk_embeddings = await embedDoc(chunks)
    await collection().add(
        ids=chunk_ids,
        embeddings=chunk_embeddings,
        documents=chunks,
        metadatas=chunk_metadata
    )
    added_check = await collection().peek()
    print(added_check)
    # return await collection().count()

async def getQueryChunks(sessionId: str, query: str):
    queryEmbedding = await embedDoc([query])
    relChunks = await collection().query(
        query_embeddings=queryEmbedding,
        n_results=5,
        where={"sessionId": sessionId},
        include=["documents", "metadatas"]
    )
    return relChunks



    
