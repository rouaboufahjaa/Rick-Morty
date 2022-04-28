"""User."""
from typing import List
from sqlalchemy.orm import Session
from security.security import hash_password
from schemas.user import UserCreateSchema, UserSchema
from models.user import User




def add_user(db_session: Session, user_data: UserCreateSchema):
    """Add user."""
    hashed_password = hash_password(user_data.password)
    db_user = User(
        email=user_data.email,
        lname=user_data.lname,
        fname=user_data.fname,
        password=hashed_password,
    )
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return db_user

def get_all_users(db_session: Session) -> List[UserSchema]:
    """Get users."""

    return db_session.query(User).all()
