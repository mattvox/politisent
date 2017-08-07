from textblob import TextBlob


def get_sentiment(tweet):
    blob = TextBlob(tweet)
    return blob.sentiment.polarity
