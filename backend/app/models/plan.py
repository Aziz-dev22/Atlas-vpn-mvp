from sqlalchemy import Column, Integer, String, Boolean, Float
from datetime import datetime

from app.db.database import Base


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    price = Column(Float, nullable=False)

    duration_days = Column(Integer, nullable=False)

    traffic_limit_gb = Column(Integer, nullable=False)

    is_active = Column(Boolean, default=True)
