from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sentivfefe.settings')

app = Celery('sentivfefe')
app.config_from_object('django.conf:settings')
# app.conf.broker_url = 'redis://localhost:6379/0'
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'fetch_and_process_tweets_each_minute': {
        'task': 'api.tasks.fetch_and_process_tweets',
        'schedule': crontab(minute=0, hour='6,9,12,15,18,21')
    },
}
