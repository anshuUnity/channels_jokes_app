from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery.decorators import periodic_task, task
from celery.task.schedules import crontab
from celery import shared_task
import requests

from celery.utils.log import get_task_logger

logger = get_task_logger('__name__')


channel_layer = get_channel_layer()


@shared_task
def get_joke_data():
    raw_data = requests.get('http://api.icndb.com/jokes/random/').json()
    joke = raw_data['value']['joke']

    async_to_sync(channel_layer.group_send)(
        'joke',
        {
            'type': 'send_joke',
            'text': joke
        }
    )
