"""Statistics."""
import pandas as pd
import numpy as np
from fastapi import HTTPException


def count_comment_for_episode():
    """Count number of comment per episode."""
    try:
        df_comment=pd.read_csv('/RickeyMorty/csv/copyComment_to.csv')
    except Exception as e_exception:
        raise HTTPException(status_code=404, detail="We don't have exported comments yet") from e_exception
    if df_comment.empty is False:
        df_comment=df_comment[df_comment['type'] == 'Episode']
        size=df_comment.groupby(['episode_id']).size()
        size.to_csv('/RickeyMorty/csv/comment_per_episode.csv')
    else:
        raise HTTPException(status_code=404, detail="We have not comments in CSV file")       
def count_letters_comments_per_episode():
    """Count number of letters in comment per episode."""
    try:
        df_comment=pd.read_csv('/RickeyMorty/csv/copyComment_to.csv')
    except Exception as e_exception:
        raise HTTPException(status_code=404, detail="We don't have exported comments yet") from e_exception
    if df_comment.empty is False:
        df_comment=df_comment[df_comment['type'] == 'Episode']
        df_comment = (df_comment.groupby('episode_id')['comment']
                                .apply(lambda x: np.mean(x.str.len()))
                                .reset_index(name='mean_len_text'))
        df_comment.to_csv('/RickeyMorty/csv/number_letter_comment_per_episode.csv')
    else:
        raise HTTPException(status_code=404, detail="We have not comments in CSV file")

def count_comments_with_rejected_status_per_episode():
    """Count the number of rejected comments."""
    try:
        df_comment=pd.read_csv('/RickeyMorty/csv/copyComment_to.csv')
    except Exception as e_exception:
        raise HTTPException(status_code=404, detail="We don't have exported comments yet") from e_exception
    if df_comment.empty is False:
        df_comment=df_comment[df_comment['type'] == 'Episode']
        df_comment=df_comment[df_comment['status'] == 'Rejected']
        size=df_comment.groupby(['episode_id']).size()
        size.to_csv('/RickeyMorty/csv/comment_with_rejected_status_per_episode.csv')
    else:
        raise HTTPException(status_code=404, detail="We have not comments in CSV file")
