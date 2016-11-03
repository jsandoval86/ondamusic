from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ondamusic.settings')

app = Celery('ondamusic')

app.config_from_object('django.conf:settings')

app.conf.update(
	BROKER_URL=os.environ.get('REDIS_URL', ''),
	CELERY_RESULT_BACKEND=os.environ.get('REDIS_URL', '')
)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
