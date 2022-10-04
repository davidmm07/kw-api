from fastapi import  FastAPI
from .config.config import initiate_database
from .routers import array as ArrayRouter , stats as StatsRouter
from .dependencies import exceptions
app = FastAPI()

@app.on_event("startup")
async def start_database():
    await initiate_database()

app.include_router(ArrayRouter.router)
app.include_router(StatsRouter.router)
exceptions.load(app)


