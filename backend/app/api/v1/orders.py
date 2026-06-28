from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.deps import get_current_user
from app.models.plan import Plan
from app.services.order_service import create_order

router = APIRouter()


@router.post("/buy/{plan_id}")
def buy_plan(
    plan_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    plan = db.query(Plan).filter(Plan.id == plan_id).first()

    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    order, subscription = create_order(
        db=db,
        user_id=user["user_id"],
        plan=plan
    )

    return {
        "message": "Purchase successful",
        "order_id": order.id,
        "subscription_id": subscription.id,
        "expires_at": subscription.end_date
    }
