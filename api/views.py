from django.shortcuts import render

from django.http import JsonResponse
# from django.http import Http404

from .models import Tweet


def index(request):
    return render(request, 'api/index.html')


def tweets(request):
    data = {'data': [{
        'id': tweet.tweet_id,
        'url': tweet.url,
        'date': tweet.date,
        'name': tweet.name,
        'twitter_name': tweet.twitter_name,
        'text': tweet.text,
        'formatted_text': tweet.formatted_text,
        'sentiment_score': tweet.sentiment_score,
    } for tweet in Tweet.objects.all()]}

    return JsonResponse(data)


# where to construct the URL? create it from models in view?
# or create it while processing data and store it in database correctly?
# url pattern: twitter.com/<twitter_name>/status/<tweet_id>

# how to display date in returned JSON object for best use with graphing?
