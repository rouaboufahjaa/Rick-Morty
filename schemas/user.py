"""User."""
from pydantic import BaseModel
from pydantic import EmailStr


class UserBase(BaseModel):
    """UserBase."""
    email: EmailStr

class UserSchema(UserBase):
    """UserSchema."""
    lname: str
    fname: str

    class Config:
        """Config."""
        orm_mode = True

class UserCreateSchema(UserSchema):
    """UserCReateSchema."""
    password: str

    class Config:
        """Config."""
        orm_mode = False
        