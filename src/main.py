from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

# Consolidated deprecated events into one lifespan function
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]
    
    yield
    
    # Shutdown logic
    app.mongo_conn.close()

# Pass lifespan to the FastAPI instance
app = FastAPI(lifespan=lifespan)

app.include_router(base.base_router)
app.include_router(data.data_router)
