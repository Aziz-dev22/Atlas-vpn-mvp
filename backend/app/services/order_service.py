from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.subscription import Subscription
from app.models.plan import Plan


def create_order(db: Session, user_id: int, plan: Plan):

    order = Order(
        user_id=user_id,
        plan_id=plan.id,
        amount=plan.price,
        status="paid"  # فعلاً شبیه‌سازی پرداخت
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    # ساخت اشتراک واقعی
    subscription = Subscription(
        user_id=user_id,
        plan_id=plan.id,
        start_date=datetime.utcnow(),
        end_date=datetime.utcnow() + timedelta(days=plan.duration_days),
        is_active=True
    )

    db.add(subscription)
    db.commit()
    db.refresh(subscription)

    return order, subscription
