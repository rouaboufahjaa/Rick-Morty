from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import mapper
from models.enums import CommentType
from models.characterWithEpisode import EpisodeCharacterRelation


class EpisodeComment(BaseModel):
    episode_id:int
    comment:str
    type:CommentType
    

class CharacterComment(BaseModel):
    character_id:int
    comment:str
    type:CommentType
   

class EpisodeCharacter(object):
    pass
mapper(EpisodeCharacter, EpisodeCharacterRelation)


class CommentBase(BaseModel):
    character_id: Optional[int] = None
    episode_id : Optional[int] = None
    type : CommentType
    comment : str
    

class CommentUpdate(BaseModel):
    comment:str

class CommentCreate(CommentBase):
    pass
class comment(CommentBase):
    id: int

    class Config:
        orm_mode = True