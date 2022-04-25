import pandas as pd
import numpy as np


def count_comment_for_episode():
    df=pd.read_csv('csv/copyComment_to.csv')
    df=df[df['type'] == 'Episode']
    size=df.groupby(['episode_id']).size()
    size.to_csv('csv/comment_per_episode.csv')
    
    
def count_letters_comments_per_episode():
    df=pd.read_csv('csv/copyComment_to.csv')
    df=df[df['type'] == 'Episode']
    df = (df.groupby('episode_id')['comment']
                            .apply(lambda x: np.mean(x.str.len()))
                            .reset_index(name='mean_len_text'))
    df.to_csv('csv/number_letter_comment_per_episode.csv')


def count_comments_with_rejected_status_per_episode():
    df=pd.read_csv('csv/copyComment_to.csv')
    df=df[df['type'] == 'Episode']
    df=df[df['status'] == 'Rejected']
    size=df.groupby(['episode_id']).size()
    size.to_csv('csv/comment_with_rejected_status_per_episode.csv')
