import os
import logging

from django.conf import settings
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
# from django.http import Http404
# from django.shortcuts import render

from .models import Tweet


class FrontendAppView(View):
    """
    Serves the frontend production entry point
    """

    def get(self, request):
        try:
            with open(
                os.path.join(
                    settings.REACT_APP_DIR,
                    'build',
                    'index.html')
            ) as home:
                return HttpResponse(home.read())
        except FileNotFoundError:
            logging.exception('Production build not found.')
            return HttpResponse(
                """
                This URL is only used for production. Visit
                http://localhost:3000/ instead, or run
                'npm run build' to test the production version
                of the app.
                """,
                status=501,
            )


class TweetsView(View):
    """
    Serves the formatted tweets as JSON
    """

    def get(self, request):
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

# def index(request):
#     return render(request, 'api/index.html')


# def tweets(request):
#     data = {'data': [{
#         'id': tweet.tweet_id,
#         'url': tweet.url,
#         'date': tweet.date,
#         'name': tweet.name,
#         'twitter_name': tweet.twitter_name,
#         'text': tweet.text,
#         'formatted_text': tweet.formatted_text,
#         'sentiment_score': tweet.sentiment_score,
#     } for tweet in Tweet.objects.all()]}
#
#     return JsonResponse(data)
