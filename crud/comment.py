from sqlalchemy.orm import Session
from fastapi import HTTPException
import pandas as pd
from schemas.comment import CommentBase, EpisodeComment,CharacterComment
from models.comment import Comment





def create_comment(db: Session, comment_data: CommentBase):
    db_Episode=Comment(character_id=comment_data.character_id,episode_id=comment_data.episode_id,type=comment_data.type,comment=comment_data.comment)
    db.add(db_Episode)
    db.commit()
    db.refresh(db_Episode)
    return db_Episode


def create_comment_episode(db: Session, comment_data: EpisodeComment):
    db_comment_episode=Comment(episode_id=comment_data.episode_id,character_id=None,type=comment_data.type,comment=comment_data.comment)
    db.add(db_comment_episode)
    db.commit()
    db.refresh(db_comment_episode)
    return db_comment_episode

def create_comment_character(db: Session, comment_data: CharacterComment):
    db_comment_character=Comment(character_id=comment_data.character_id,episode_id=None,type=comment_data.type,comment=comment_data.comment)
    db.add(db_comment_character)
    db.commit()
    db.refresh(db_comment_character)
    return db_comment_character



def get_comment(db: Session):
    comment=db.query(Comment.character_id,Comment.episode_id,Comment.type,Comment.comment,Comment.status).all()
    df = pd.DataFrame(comment, columns=['character_id','episode_id','type','comment','status'])
    df.to_csv('csv/copyComment_to.csv',index=True)