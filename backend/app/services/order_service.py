from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.subscription import Subscription
from app.models.plan import Plan
from app.services.marzban_service import MarzbanService


async def create_order(db: Session, user_id: int, plan: Plan):

    # 1. ساخت سفارش
    order = Order(
        user_id=user_id,
        plan_id=plan.id,
        amount=plan.price,
        status="paid"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    # 2. ساخت اشتراک
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

    # 3. ساخت کاربر VPN در Marzban
    vpn = MarzbanService()

    vpn_user = await vpn.create_user(
        username=f"user_{user_id}",
        expire_days=plan.duration_days
    )

    return {
        "order": order,
        "subscription": subscription,
        "vpn_user": vpn_user
    }
