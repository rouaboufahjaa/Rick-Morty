"""User."""
from sqlalchemy import Column, Integer, String
from config.database import engine, Base

class User(Base):
    """User."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lname = Column(String(115), unique=False, index=False, nullable=True)
    fname = Column(String(115), unique=False, index=False, nullable=True)
    email = Column(String(115), unique=False, index=False, nullable=True)
    password=Column(String(115), unique=False, index=False, nullable=True)



Base.metadata.create_all(engine)
