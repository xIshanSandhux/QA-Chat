# will be using BAAI embedding model for the embedding 

from sentence_transformers import SentenceTransformer
from typing import List

# global variable for the model
model = None

# embedding the chunks
def embedDoc(chunks: List[str]):
    global model
    if model is None:
        initializeEmbedModel()
    embeddings = model.encode_document(chunks, batch_size=8)
    return embeddings

# embedding the query
def embedQuery(query: str):
    global model
    if model is None:
        initializeEmbedModel()
    embeddings = model.encode_query(query,batch_size=4)
    return embeddings

# initializing the embed model
def initializeEmbedModel():
    global model
    if model is None:
        model = SentenceTransformer('BAAI/bge-base-en-v1.5')
    return model