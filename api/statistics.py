from fastapi import APIRouter
from config.database import SessionLocal
from crud.statisticsComment import count_comment_for_episode, count_letters_comments_per_episode, count_comments_with_rejected_status_per_episode


app = APIRouter()
session=SessionLocal()
@app.get('/exportCommentPerEpisode')
def count_comment_per_episode():
    count_comment_for_episode()
    return {'message': 'Comments per episode are exported into csv'}

@app.get('/exportLetterCommentPerEpisode')
def count_letters_comments_episode():
    count_letters_comments_per_episode()
    return {'message': "Mean of letter's length in comment is exported"}

@app.get('/exportCommentsWithRejectedStatus')
def count_comments_with_rejected_status():
    count_comments_with_rejected_status_per_episode()
    return {'message': 'Comments with status rejected per episode are exported into csv'}