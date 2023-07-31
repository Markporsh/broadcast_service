import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'broadcast_service.settings')

app = Celery('broadcast_service', broker='redis://redis:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()
