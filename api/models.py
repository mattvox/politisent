from django.db import models
from django.core.validators import URLValidator

# Create your models here.


class Tweet(models.Model):
    """
    Model for each formatted Tweet
    """

    def __str__(self):
        return self.tweet_id

    tweet_id = models.IntegerField(unique=True)
    url = models.CharField(validators=[URLValidator], max_length=1000,
                           unique=True)
    name = models.CharField(max_length=128)
    twitter_name = models.CharField(max_length=128, unique=True)

    text = models.CharField(max_length=256)

# Tweet
# - Tweet ID
# - Tweet URL
# - Username - both name and @name
# - Date
# - Sentiment Score
# - Confidence Score
# - Tweet text
# - Retweets?
# - Favorites?
