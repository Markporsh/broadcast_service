from __future__ import absolute_import, unicode_literals
# Этот обеспечивает, что приложение всегда импортируется, когда Django запускается,
# поэтому shared_task будет использовать это приложение.
from celery_app import app as celery_app
from broadcast import tasks  # noqa
__all__ = ('celery_app',)
