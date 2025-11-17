import redis.asyncio as redis
from typing import Optional
from app.core.config import settings

redis_client: Optional[redis.Redis] = None


async def get_redis() -> redis.Redis:
    if redis_client is None:
        raise RuntimeError("Redis client not initialized")
    return redis_client


async def init_redis() -> None:
    global redis_client
    redis_client = redis.from_url(
        settings.REDIS_URL,
        encoding="utf-8",
        decode_responses=True
    )


async def close_redis() -> None:
    global redis_client
    if redis_client:
        await redis_client.close()
        redis_client = None


async def check_redis_health() -> bool:
    try:
        if redis_client:
            await redis_client.ping()
            return True
        return False
    except Exception:
        return False
