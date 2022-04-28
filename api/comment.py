'''comment'''
from fastapi import APIRouter
from fastapi_pagination import  Page, add_pagination, paginate
from config.database import SessionLocal
from schemas.comment import CommentSchema, CommentBase, EpisodeComment, CharacterComment, CommentUpdate
from crud.comment import create_comment, create_comment_episode, create_comment_character
from models.comment import Comment


app = APIRouter()
session=SessionLocal()
@app.post("/commentsCharactersEpisodes/", response_model=CommentSchema)
def add_comment(comment_data:CommentBase):
    """Add a comment for character in episode."""
    comment_data= create_comment(session, comment_data)
    return comment_data

@app.post('/addCommentEpisode')
def create_episode_comment(episode_comment:EpisodeComment):
    """Add a comment for episode."""
    comment_episode=create_comment_episode(session,episode_comment)
    return comment_episode

@app.post('/addCommentCharacter')
def add_character_comment(character_comment:CharacterComment):
    """Add a comment for character."""
    comment_character=create_comment_character(session,character_comment)
    return comment_character

@app.get("/comments/page", response_model=Page[CommentSchema])
def get_comments():
    """Add pagination."""
    db_comments = session.query(Comment).all()
    return paginate(db_comments)

@app.get("/comments/{id}", response_model=CommentSchema)
def get_comments_by_id(id_comment:int):
    """Get comments by id."""
    db_comments = session.query(Comment).get(id_comment)
    return db_comments

@app.delete("/comment/{id}")
def delete_comment_info(id_comment: int):
    """Delete Comments by id."""
    comment_info = session.query(Comment).get(id_comment)
    session.delete(comment_info)
    session.commit()
    return {'message': 'The comment is deleted successfully'}

@app.put("/comment/{id}")
def update_comment(id_comment: int, comment_update: CommentUpdate)->Comment:
    """Modify comments."""
    comment_info = session.query(Comment).get(id_comment)
    comment_info.comment = comment_update.comment
    session.commit()
    session.refresh(comment_info)
    return comment_info



add_pagination(app)
