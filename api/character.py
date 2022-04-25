from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import  Page, add_pagination, paginate
from config.database import SessionLocal
from typing import List, Optional
from models.characterWithEpisode import Character
from schemas.character import character, CharacterCreate


app = APIRouter()
session=SessionLocal()

@app.get("/characters", response_model=List[character])
def get_characters(skip: int = 0, limit: int = 100):
    db_characters = session.query(Character).offset(skip).limit(limit).all()
    return db_characters

@app.get("/characters/page", response_model=Page[character])
def get_characters():
    db_characters = session.query(Character).all()
    return paginate(db_characters)

@app.get("/characters/")
def get_character(name: Optional[str] = None,status: Optional[str] = None, species:Optional[str] = None, type:Optional[str] = None, gender:Optional[str] = None):
    params = locals().copy()
    query = session.query(Character)
    for attr in [x for x in params if params[x] is not None]:query = query.filter(getattr(Character, attr).like(params[attr])) 
    session.commit()
    return query.all()

add_pagination(app)