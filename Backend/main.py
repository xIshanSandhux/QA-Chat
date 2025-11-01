from fastapi import FastAPI
import redis
from api.Routes.idroutes import router as idroute
from api.Routes.chatroute import router as chatroute
from api.redis.initialization import start_redis, shutdown_redis
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # redis for the chat history
    await start_redis()
    yield
    
    await shutdown_redis()

app = FastAPI(title="QA Chat API", lifespan=lifespan)
app.include_router(idroute)
app.include_router(chatroute)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
allow_headers=["*"],
)