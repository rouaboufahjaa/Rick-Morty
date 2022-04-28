"""Character in crud."""
from sqlalchemy.orm import Session
from schemas.character import CharacterCreate
from models.character_with_episode import Character




def create_character(db_session: Session, chr_data: CharacterCreate):
    """Add character."""
    db_character = Character(name=chr_data.name,status=chr_data.status,species=chr_data.species,type=chr_data.type,gender=chr_data.gender)
    db_session.add(db_character)
    db_session.commit()
    db_session.refresh(db_character)
    return db_character
    