from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "Atlas VPN",
        "version": "1.0.0"
    }
