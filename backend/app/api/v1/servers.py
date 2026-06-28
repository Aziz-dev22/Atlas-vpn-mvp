from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.server import ServerCreate, ServerOut
from app.services.server_service import create_server, get_servers
from app.core.deps import get_current_user

router = APIRouter()


@router.post("/servers", response_model=ServerOut)
def add_server(
    server: ServerCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_server(db, server)


@router.get("/servers", response_model=list[ServerOut])
def list_servers(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_servers(db)
