from pydantic import BaseModel


class episodeCharacterRelationCreate(BaseModel):
    character_id: int
    episode_id : int