from fastapi import FastAPI
from contextlib import asynccontextmanager
from views import router
from redis_client import init_redis, close_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event: Initialize Redis
    await init_redis()
    yield
    # Shutdown event: Close Redis
    await close_redis()

app = FastAPI(title="Async Processing Service", version="1.0", lifespan=lifespan)
app.include_router(router)
