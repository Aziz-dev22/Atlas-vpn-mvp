from pydantic import BaseModel


class ServerCreate(BaseModel):
    name: str
    host: str
    port: int = 22
    username: str | None = None
    password: str | None = None


class ServerOut(BaseModel):
    id: int
    name: str
    host: str
    port: int
    is_active: bool

    class Config:
        from_attributes = True
