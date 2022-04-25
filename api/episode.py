from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from models.characterWithEpisode import Episode
from schemas.episode import episode, EpisodeCreate
from typing import List

app = APIRouter()
session=SessionLocal()

@app.get("/episodes", response_model=List[episode])
def get_episodes(skip: int = 0, limit: int = 100):
    db_episodes = session.query(Episode).offset(skip).limit(limit).all()
    return db_episodes