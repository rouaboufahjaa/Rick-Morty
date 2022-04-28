"""Character in episode in crud."""
from config.database import SessionLocal
from schemas.character_episode import EpisodeCharacterRelationCreate
from models.character_with_episode import EpisodeCharacterRelation






session=SessionLocal()
def create_episode_character_relation(ep_chr_data: EpisodeCharacterRelationCreate):
    """Create character in episode relation."""
    episode_character = EpisodeCharacterRelation.insert().values(character_id=ep_chr_data.character_id, episode_id=ep_chr_data.episode_id)
    session.execute(episode_character)
    session.commit()
    return ep_chr_data
