from fastapi import FastAPI
from api.Routes.idroutes import router as idroute
from api.Routes.chatroute import router as chatroute


app = FastAPI(title="QA Chat API")
app.include_router(idroute)
app.include_router(chatroute)