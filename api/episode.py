'''episode.'''
from typing import List
from fastapi import APIRouter
from config.database import SessionLocal
from models.character_with_episode import Episode
from schemas.episode import EpisodeSchema

app = APIRouter()
session=SessionLocal()

@app.get("/episodes", response_model=List[EpisodeSchema])
def get_episodes(skip: int = 0, limit: int = 100):
    """Get episodes"""
    db_episodes = session.query(Episode).offset(skip).limit(limit).all()
    return db_episodes
