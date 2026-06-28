from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from datetime import datetime

from app.db.database import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    plan_id = Column(Integer, ForeignKey("plans.id"))

    start_date = Column(DateTime, default=datetime.utcnow)

    end_date = Column(DateTime, nullable=False)

    is_active = Column(Boolean, default=True)
