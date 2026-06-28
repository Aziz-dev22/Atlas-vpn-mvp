from pydantic import BaseModel


class UserCreate(BaseModel):
    telegram_id: str
    username: str | None = None
    full_name: str | None = None


class UserOut(BaseModel):
    id: int
    telegram_id: str
    username: str | None
    full_name: str | None
    is_active: bool
    is_premium: bool

    class Config:
        from_attributes = True
