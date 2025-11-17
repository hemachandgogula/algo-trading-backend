from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db import get_db
from app.core.cache import check_redis_health

router = APIRouter()


@router.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    db_status = "down"
    cache_status = "down"

    try:
        result = await db.execute(text("SELECT 1"))
        if result.scalar() == 1:
            db_status = "up"
    except Exception:
        pass

    cache_status = "up" if await check_redis_health() else "down"

    overall_status = "ok" if db_status == "up" and cache_status == "up" else "degraded"

    return {
        "status": overall_status,
        "services": {
            "database": db_status,
            "cache": cache_status
        }
    }
