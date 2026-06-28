from sqlalchemy.orm import Session

from app.models.plan import Plan
from app.schemas.plan import PlanCreate


def create_plan(db: Session, plan_data: PlanCreate):

    plan = Plan(
        name=plan_data.name,
        price=plan_data.price,
        duration_days=plan_data.duration_days,
        traffic_limit_gb=plan_data.traffic_limit_gb,
    )

    db.add(plan)
    db.commit()
    db.refresh(plan)

    return plan


def get_plans(db: Session):
    return db.query(Plan).filter(Plan.is_active == True).all()
