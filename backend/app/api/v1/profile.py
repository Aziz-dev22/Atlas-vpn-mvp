from fastapi import APIRouter, Depends

from app.core.deps import get_current_user

router = APIRouter()


@router.get("/profile")
def profile(current_user=Depends(get_current_user)):

    return {
        "message": "Protected route accessed",
        "user": current_user
    }
