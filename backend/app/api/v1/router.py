from fastapi import APIRouter

from app.api.v1.users import router as users_router
from app.api.v1.auth import router as auth_router
from app.api.v1.profile import router as profile_router
from app.api.v1.servers import router as servers_router
from app.api.v1.plans import router as plans_router

router = APIRouter()

router.include_router(users_router)
router.include_router(auth_router)
router.include_router(profile_router)
router.include_router(servers_router)
router.include_router(plans_router)
