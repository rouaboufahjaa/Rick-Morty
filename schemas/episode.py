from typing import Optional
from pydantic import BaseModel


class EpisodeBase(BaseModel):
    #id : int
    name: str
    air_date : str
    episode : str
    description : Optional[str] = None

class EpisodeCreate(EpisodeBase):
    pass
class episode(EpisodeBase):
    id: int

    class Config:
        orm_mode = True