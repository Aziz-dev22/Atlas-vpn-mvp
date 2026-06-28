from sqlalchemy import Column, Integer, ForeignKey, Float, String, DateTime
from datetime import datetime

from app.db.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    plan_id = Column(Integer, ForeignKey("plans.id"))

    amount = Column(Float, nullable=False)

    status = Column(String, default="pending")  # pending, paid, failed

    created_at = Column(DateTime, default=datetime.utcnow)
