import logging
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from celery import shared_task
from django.apps import apps

logger = logging.getLogger(__name__)


@shared_task
def send_newsletter(newsletter_id):
    newsletter_model = apps.get_model('broadcast', 'Newsletter')
    message_model = apps.get_model('broadcast', 'Message')
    try:
        newsletter = newsletter_model.objects.get(id=newsletter_id)
    except ObjectDoesNotExist:
        logger.error(f"Рассылка {newsletter_id} не найдена в базе данных")
        return

    clients = newsletter.get_clients()

    for client in clients:
        message_model.objects.create(newsletter=newsletter, client=client)
        logging.info(f"Отправка сообщения клиенту {client.id} по рассылке {newsletter.id}")

    newsletter.end_date = timezone.now()
    newsletter.save()

