"""Comment."""
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import mapper
from models.enums import CommentType, StatusType
from models.character_with_episode import EpisodeCharacterRelation


class EpisodeComment(BaseModel):
    """EpisodeComment."""
    episode_id:int
    comment:str
    type:CommentType
    status:StatusType

class CharacterComment(BaseModel):
    "CharacterComment."
    character_id:int
    comment:str
    type:CommentType
    status:StatusType

class EpisodeCharacter(object):
    """EpisodeCharacter."""
    pass
mapper(EpisodeCharacter, EpisodeCharacterRelation)


class CommentBase(BaseModel):
    """CommentBase."""
    character_id: Optional[int] = None
    episode_id : Optional[int] = None
    type : CommentType
    comment : str
    status:StatusType

class CommentUpdate(BaseModel):
    """CommentUpdate."""
    comment:str

class CommentCreate(CommentBase):
    """CommentCreate."""
    pass
class CommentSchema(CommentBase):
    """CommentSchema."""
    id: int

    class Config:
        """Config."""
        orm_mode = True
