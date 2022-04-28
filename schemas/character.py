"""Character."""
from typing import List
from pydantic import BaseModel
from schemas.episode import EpisodeSchema

class CharacterBase(BaseModel):
    """CharacterBase."""
    name : str
    status : str
    species : str
    type : str
    gender : str

class CharacterCreate(CharacterBase):
    """CharacterCreate."""
    episode_ids: List[int] = []

class CharacterSchema(CharacterBase):
    """Character."""
    episodes: List[EpisodeSchema] = []

    class Config:
        """Config."""
        orm_mode = True
