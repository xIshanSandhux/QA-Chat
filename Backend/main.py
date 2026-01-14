from fastapi import FastAPI
# import redis
from api.Routes.idroutes import router as idroute
# from api.Routes.chatroute import router as chatroute
# from api.Routes.fileUpload import router as fileUpload
# from api.redis.initialization import start_redis, shutdown_redis
from Infra.redis.initialization import start_redis,shutdown_redis
from vectorDB.chromaDB.startup import start_chromadb, shutdown_chromadb
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
# from LLM.factory import LLMProviderFactory
from src.routes.chat import router as chatroute
from src.services.LLM.factory import LLMProviderFactory
from RAG.embedding.embed import initializeEmbedModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    # redis for the chat history
    await start_redis()
    await start_chromadb()
    # LLM provider initialization
    provider = LLMProviderFactory()
    initializeEmbedModel()
    print(provider)
    yield
    await shutdown_redis()
    await shutdown_chromadb()

app = FastAPI(title="QA Chat API", lifespan=lifespan)
app.include_router(idroute)
app.include_router(chatroute)
# app.include_router(fileUpload)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
allow_headers=["*"],
)