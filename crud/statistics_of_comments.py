"""Statistics."""
import pandas as pd
import numpy as np


def count_comment_for_episode():
    """Count number of comment per episode."""
    df=pd.read_csv('csv/copyComment_to.csv')
    df=df[df['type'] == 'Episode']
    size=df.groupby(['episode_id']).size()
    size.to_csv('csv/comment_per_episode.csv')

def count_letters_comments_per_episode():
    """Count number of letters in comment per episode."""
    df_comment=pd.read_csv('csv/copyComment_to.csv')
    df_comment=df_comment[df_comment['type'] == 'Episode']
    df_comment = (df_comment.groupby('episode_id')['comment']
                            .apply(lambda x: np.mean(x.str.len()))
                            .reset_index(name='mean_len_text'))
    df_comment.to_csv('csv/number_letter_comment_per_episode.csv')

def count_comments_with_rejected_status_per_episode():
    """Count the number of rejected comments."""
    df_comment=pd.read_csv('csv/copyComment_to.csv')
    df_comment=df_comment[df_comment['type'] == 'Episode']
    df_comment=df_comment[df_comment['status'] == 'Rejected']
    size=df_comment.groupby(['episode_id']).size()
    size.to_csv('csv/comment_with_rejected_status_per_episode.csv')
