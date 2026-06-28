from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import get_or_create_user

router = APIRouter()


@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    db_user = get_or_create_user(db, user)

    return db_user
