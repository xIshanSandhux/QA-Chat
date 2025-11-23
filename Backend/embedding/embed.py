# will be using BAAI embedding model for the embedding 

from sentence_transformers import SentenceTransformer
from typing import List

async def embedDoc(chunks: List[str]):
    model = SentenceTransformer('BAAI/bge-base-en-v1.5')
    embeddings = model.encode(chunks)
    return embeddings
