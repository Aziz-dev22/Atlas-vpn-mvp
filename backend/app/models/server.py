from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from app.db.database import Base


class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    host = Column(String, nullable=False)

    port = Column(Integer, default=22)

    username = Column(String, nullable=True)

    password = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)
