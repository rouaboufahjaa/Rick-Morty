"""Character with episode."""
from pydantic import BaseModel


class EpisodeCharacterRelationCreate(BaseModel):
    """Character and episode relation."""
    character_id: int
    episode_id : int
