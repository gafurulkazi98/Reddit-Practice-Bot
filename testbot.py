# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:12:26 2019

@author: Rafi
"""

import praw

reddit = praw.Reddit(client_id='TXOlydHdWp9zbA',
                     client_secret='TFwBuAIZ-sHRMaLVBoGzVSXP514',
                     user_agent='practicebotv1 by Penguinmanereikel',
                     username='reddit_bot_practice',
                     password='bot_to_practice_with')
                     
subreddit = reddit('SubredditSimulator')

subreddit_h = subreddit()

for submission in subreddit_h:
    print(submission.title)