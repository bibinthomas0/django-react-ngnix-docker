from celery import shared_task
import logging
from datetime import datetime
from .models import Posts

@shared_task
def check_post_validity():
    try:
        logging.info('Starting check_post_validity task...')
        now = datetime.now()
        expired_posts = Posts.objects.filter(valid_till__lt=now, is_active=True)

        for post in expired_posts:
            post.is_active = False
            post.save()

        logging.info('Task completed successfully.')
    except Exception as e:
        logging.error(f"An error occurred: {e}")
