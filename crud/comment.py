"""Comment in crud."""
from sqlalchemy.orm import Session
import pandas as pd
from schemas.comment import CommentBase, EpisodeComment,CharacterComment
from models.comment import Comment





def create_comment(db_session: Session, comment_data: CommentBase):
    """Add comment for character in episode."""
    db_episode=Comment(character_id=comment_data.character_id,episode_id=comment_data.episode_id,type=comment_data.type,comment=comment_data.comment,status=comment_data.status)
    db_session.add(db_episode)
    db_session.commit()
    db_session.refresh(db_episode)
    return db_episode


def create_comment_episode(db_session: Session, comment_data: EpisodeComment):
    """Add comment for episode."""
    db_comment_episode=Comment(episode_id=comment_data.episode_id,character_id=None,type=comment_data.type,comment=comment_data.comment,status=comment_data.status)
    db_session.add(db_comment_episode)
    db_session.commit()
    db_session.refresh(db_comment_episode)
    return db_comment_episode

def create_comment_character(db_session: Session, comment_data: CharacterComment):
    """Add character for character."""
    db_comment_character=Comment(character_id=comment_data.character_id,episode_id=None,type=comment_data.type,comment=comment_data.comment,status=comment_data.status)
    db_session.add(db_comment_character)
    db_session.commit()
    db_session.refresh(db_comment_character)
    return db_comment_character



def get_exported_comment(db_session: Session):
    """Get comments."""
    comment=db_session.query(Comment.character_id,Comment.episode_id,Comment.type,Comment.comment,Comment.status).all()
    df_comment = pd.DataFrame(comment, columns=['character_id','episode_id','type','comment','status'])
    df_comment.to_csv('/RickeyMorty/csv/copyComment_to.csv',index=True)
