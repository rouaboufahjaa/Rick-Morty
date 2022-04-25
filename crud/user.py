from typing import List
from sqlalchemy.orm import Session
from security.security import hash_password
from schemas.user import UserCreateSchema, UserSchema
from models.user import User




def add_user(db: Session, user_data: UserCreateSchema):
    hashed_password = hash_password(user_data.password)
    db_user = User(
        email=user_data.email,
        lname=user_data.lname,
        fname=user_data.fname,
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session) -> List[UserSchema]:
    return db.query(User).all()