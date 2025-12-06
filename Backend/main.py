from fastapi import FastAPI
import redis
from api.Routes.idroutes import router as idroute
from api.Routes.chatroute import router as chatroute
from api.Routes.fileUpload import router as fileUpload
from api.redis.initialization import start_redis, shutdown_redis
from vectorDB.chromaDB.startup import start_chromadb
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from LLM.LLMConfig import get_LLMConfig


@asynccontextmanager
async def lifespan(app: FastAPI):
    # redis for the chat history
    await start_redis()
    await start_chromadb()
    yield
    
    await shutdown_redis()

app = FastAPI(title="QA Chat API", lifespan=lifespan)
print(get_LLMConfig())
app.include_router(idroute)
app.include_router(chatroute)
app.include_router(fileUpload)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
allow_headers=["*"],
)