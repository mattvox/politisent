from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task(bind=True)
def test_task(self):
    print('Test task!')
