from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def get_or_create_user(db: Session, user_data: UserCreate):
    user = db.query(User).filter(
        User.telegram_id == user_data.telegram_id
    ).first()

    if user:
        return user

    new_user = User(
        telegram_id=user_data.telegram_id,
        username=user_data.username,
        full_name=user_data.full_name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
