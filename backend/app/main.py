from fastapi import FastAPI

from app.api.v1.router import router
from app.core.config import settings
from app.db.database import Base, engine

app = FastAPI(
    title=settings.APP_NAME
)

# ساخت جدول‌ها
Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Atlas VPN Backend Running"}
