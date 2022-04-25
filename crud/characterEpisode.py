from sqlalchemy.orm import Session
from config.database import SessionLocal
from schemas.characterEpisode import episodeCharacterRelationCreate
from models.characterWithEpisode import EpisodeCharacterRelation






session=SessionLocal()
def create_episodeCharacterRelation(db: Session, epChr_data: episodeCharacterRelationCreate):
    episode_character = EpisodeCharacterRelation.insert().values(character_id=epChr_data.character_id, episode_id=epChr_data.episode_id)
    session.execute(episode_character)
    session.commit()
    return epChr_data

