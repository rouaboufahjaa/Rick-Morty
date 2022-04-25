from sqlalchemy.orm import Session
from config.database import SessionLocal
from schemas.characterEpisode import episodeCharacterRelationCreate
from models.characterWithEpisode import EpisodeCharacterRelation






session=SessionLocal()
def create_episode_character_relation(db: Session, ep_chr_data: episodeCharacterRelationCreate):
    episode_character = EpisodeCharacterRelation.insert().values(character_id=ep_chr_data.character_id, episode_id=ep_chr_data.episode_id)
    session.execute(episode_character)
    session.commit()
    return ep_chr_data

