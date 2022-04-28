"""Episode."""
from typing import Optional
from pydantic import BaseModel


class EpisodeBase(BaseModel):
    """EpisodeBase."""
    name: str
    air_date : str
    episode : str
    description : Optional[str] = None

class EpisodeCreate(EpisodeBase):
    """EpisodeCreate."""
    pass
class EpisodeSchema(EpisodeBase):
    """Episode"""
    id: int

    class Config:
        """Config."""
        orm_mode = True
