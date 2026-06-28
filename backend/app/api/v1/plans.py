from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.plan import PlanCreate, PlanOut
from app.services.plan_service import create_plan, get_plans
from app.core.deps import get_current_user

router = APIRouter()


@router.post("/plans", response_model=PlanOut)
def add_plan(
    plan: PlanCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_plan(db, plan)


@router.get("/plans", response_model=list[PlanOut])
def list_plans(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_plans(db)
