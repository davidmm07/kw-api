from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from mongomock_motor import AsyncMongoMockClient
from ..models.record import Record
import os

class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL", "")
    ENVIRONMENT: Optional[str] = os.getenv("ENVIRONMENT", "test")


async def initiate_database():
    client = AsyncMongoMockClient() if Settings().ENVIRONMENT.lower().startswith("test") else AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(database=client.get_default_database(),
                      document_models=[Record])