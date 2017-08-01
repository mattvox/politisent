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
        'name': tweet.name,
        'twitter_name': tweet.twitter_name,
        'text': tweet.text,
    } for tweet in Tweet.objects.all()]}

    return JsonResponse(data)
