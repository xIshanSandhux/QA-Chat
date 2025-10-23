from fastapi import FastAPI
from api.Routes.idroutes import router as idroute



app = FastAPI(title="QA Chat API")
app.include_router(idroute)