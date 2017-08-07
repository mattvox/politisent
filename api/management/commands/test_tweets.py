from .get_tweets import get_tweets
from django.core.management.base import BaseCommand, CommandError

search_term = 'Trump -filter:retweets'
tweet_count = 100


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_tweets(search_term, tweet_count)
