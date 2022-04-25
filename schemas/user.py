from pydantic import BaseModel
from pydantic import EmailStr


class UserBase(BaseModel):
   email: EmailStr
class UserSchema(UserBase):
   lname: str
   fname: str

   class Config:
        orm_mode = True

class UserCreateSchema(UserSchema):
    password: str

    class Config:
        orm_mode = False

