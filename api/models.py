from django.db import models
from django.core.validators import URLValidator


class Tweet(models.Model):
    """
    Model for each tweet
    """

    def __str__(self):
        return str(self.tweet_id)

    tweet_id = models.CharField(max_length=255, unique=True)
    url = models.CharField(validators=[URLValidator], max_length=1000,
                           unique=True)
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=128)
    twitter_name = models.CharField(max_length=128, unique=True)
    text = models.TextField(default='')
    formatted_text = models.TextField(default='')
    sentiment_score = models.DecimalField(max_digits=3, decimal_places=2,
                                          default=0)
    # confidence_score = models.DecimalField(max_digits=3, decimal_places=2,
    #                                        default=0)


# datetime.datetime(2017, 8, 3, 23, 10, 19, 184107, tzinfo=<UTC>)

# 'Tue Jan 24 09:37:52 +0000 2017'

# strip out the day of the week, grab month and assign it a numerical value, grab day, grab year, then move onto time

#

# datetime.strptime(time_str, '%a %b %d %H:%M:%S %z %Y').replace(tzinfo=timezone.utc).astimezone(tz=None).strftime('%Y-%m-%d %H:%M:%S')

# retweet_count = models.IntegerField(default=0)
# favorite_count = models.IntegerField(default=0)
