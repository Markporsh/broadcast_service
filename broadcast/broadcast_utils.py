from django.utils import timezone
from .models import Newsletter
from celery import current_app


def send_newsletter_on_save(newsletter_id):
    newsletter = Newsletter.objects.get(id=newsletter_id)
    now = timezone.now()
    if newsletter.start_date <= now <= newsletter.end_date:
        current_app.send_task('broadcast.tasks.send_newsletter', args=[newsletter.id])
    elif newsletter.start_date > now:
        delay = (newsletter.start_date - now).total_seconds()
        current_app.send_task('broadcast.tasks.send_newsletter', args=[newsletter.id], countdown=delay)
