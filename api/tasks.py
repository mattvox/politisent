import logging
# from __future__ import absolute_import, unicode_literals

from sentivfefe.celery import app
from api.management.commands import get_tweets


@app.task
def fetch_and_process_tweets():
    search_term = 'Trump -filter:retweets'
    tweet_count = 100
    get_tweets.get_tweets(search_term, tweet_count)
