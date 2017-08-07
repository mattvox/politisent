import tweepy
from django.db.utils import IntegrityError

from api.models import Tweet
from .get_sentiment import get_sentiment


def get_tweets(search_term, tweet_count):
    consumer_key = '7bdUIEJDOLveAiWuHK4dxQDqC'
    consumer_secret = 'wrvb59PcIjOP5kuQlmQYqmU3fo5GIMps3OnCmfT3aNNtKIFaGw'
    access_token = '1873426352-gvELy2xJU4VKazKnu1v2QgYWknpgovDktkCHDdU'
    access_token_secret = 'v8oHQs80fDTZbu16AGDOYYZlAyOIIjPo7o6seRme5glnl'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets = api.search(search_term, count=tweet_count, lang='en',
                        show_user=True, tweet_mode='extended')

    for tweet in tweets:

        try:
            formatted_tweet = Tweet(
                tweet_id=tweet.id,
                date=tweet.created_at,
                name=tweet.user.name,
                twitter_name=tweet.user.screen_name,
                text=tweet.full_text,
                url='https://twitter.com/' + tweet.user.screen_name + '/status/' + str(tweet.id),
                sentiment_score=get_sentiment(tweet.full_text)
            )

            formatted_tweet.save()
            print('Tweet ' + str(tweet.id) + ' saved!')

        except IntegrityError:
            print('An error occured...')
            pass


# check_status = api.statuses_lookup([893307460731248640])
# print(check_status[0].retweet_count)

#
# for tweet in trump_tweets:
#     json_tweet = tweet._json
#     formatted_tweets.append(json_tweet['text'])

# for index, tweet in enumerate(trump_tweets):
#     if index < 1:
#         print(tweet._json)

# print(trump_tweets[0]._json)

# for index, tweet in enumerate(formatted_tweets):
#     # if index < 10:
#     print(index, ':', tweet, '\n')

# print(type(trump_tweets))

# print(trump_tweets)

# print(dir(trump_tweets))

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
