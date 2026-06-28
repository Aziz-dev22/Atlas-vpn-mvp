from pydantic import BaseModel


class PlanCreate(BaseModel):
    name: str
    price: float
    duration_days: int
    traffic_limit_gb: int


class PlanOut(BaseModel):
    id: int
    name: str
    price: float
    duration_days: int
    traffic_limit_gb: int
    is_active: bool

    class Config:
        from_attributes = True
