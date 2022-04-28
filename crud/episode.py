"""Episode in crud."""
from sqlalchemy.orm import Session
from config.database import SessionLocal
from schemas.episode import EpisodeCreate
from models.character_with_episode import Episode

session=SessionLocal()
def create_episode(db_session: Session, ep_data: EpisodeCreate):
    """Add episode."""
    db_episode=Episode(id=ep_data.id,name=ep_data.name,air_date=ep_data.air_date,episode=ep_data.episode)
    db_session.add(db_episode)
    db_session.commit()
    db_session.refresh(db_episode)
    return db_episode


def add_description_episode(title:str,description:str):
    """Add description for episode."""
    episode_info  = session.query(Episode).filter(Episode.name== title).all()
    for info in episode_info:
        if info:
            info.description=description
            session.commit()
            session.refresh(info)
