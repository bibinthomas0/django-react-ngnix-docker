from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

celery_app = Celery('backend')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()



celery_app.conf.beat_schedule = {
    'check-post-validity': {
        'task': 'userpost.tasks.check_post_validity',
        'schedule': crontab(), 
    },
}

