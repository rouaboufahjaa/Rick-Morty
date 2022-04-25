from sqlalchemy.orm import Session
from schemas.character import CharacterCreate
from models.characterWithEpisode import Character




def create_character(db: Session, chr_data: CharacterCreate):
    db_character = Character(id=chr_data.id,name=chr_data.name, status=chr_data.status,species=chr_data.species,type=chr_data.type,gender=chr_data.gender)
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character