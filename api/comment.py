from fastapi import APIRouter
from fastapi_pagination import  Page, add_pagination, paginate
from config.database import SessionLocal
from schemas.comment import comment, CommentBase, EpisodeComment, CharacterComment, CommentUpdate
from crud.comment import create_comment, create_comment_episode, create_comment_character, get_comment
from models.comment import Comment
from starlette.responses import Response


app = APIRouter()
session=SessionLocal()
@app.post("/commentsCharactersEpisodes/", response_model=comment)
def add_comment(comment_data:CommentBase):  
	comment_data= create_comment(session, comment_data)
	return comment_data

@app.get("/comments/page", response_model=Page[comment])
def get_comments():
    db_comments = session.query(Comment).all()
    return paginate(db_comments)

@app.post('/addCommentEpisode')
def create_episode_comment(comment:EpisodeComment):
    comment_episode=create_comment_episode(session,comment)
    return comment_episode


@app.post('/addCommentCharacter')
def create_episode_comment(comment:CharacterComment):
    comment_character=create_comment_character(session,comment)
    return comment_character



@app.get("/comments/{id}", response_model=comment)
def get_comments(id:int):
    db_comments = session.query(Comment).get(id)
    return db_comments


@app.delete("/comment/{id}")
def delete_user_info(id: int):
    try:
        comment_info = session.query(Comment).get(id)
        session.delete(comment_info)
        session.commit()
        return {'message': 'The comment is deleted successfully'}
    except Exception:
        return Response("Internal server error", status_code=500)


@app.put("/comment/{id}")
def update_comment(id: int, comment_update: CommentUpdate)->Comment:
    try:
        comment_info = session.query(Comment).get(id)
        comment_info.comment = comment_update.comment
        session.commit()
        session.refresh(comment_info)
        return comment_info
    except Exception:
        return Response("Internal server error", status_code=500)

@app.get('/exportComments/')
def export_comments():
    get_comment(session)
    return {'message': 'Comments are exported into csv'}



add_pagination(app)




