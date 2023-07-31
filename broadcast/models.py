import uuid
from django.db import models
from django.utils import timezone
from broadcast.tasks import send_newsletter
from celery import current_app


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=11)
    mobile_operator_code = models.IntegerField()
    tag = models.CharField(max_length=100, blank=True, null=True)


class Newsletter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateTimeField()
    message_text = models.TextField()
    mobile_operator_code = models.IntegerField(blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    end_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        now = timezone.now()
        if self.start_date <= now <= self.end_date:
            send_newsletter.delay(self.id)
        elif self.start_date > now:
            delay = (self.start_date - now).total_seconds()
            current_app.send_task('broadcast.tasks.send_newsletter', args=[self.id], countdown=delay)

    def get_clients(self):
        if self.mobile_operator_code and self.tag:
            # Если задан код мобильного оператора и тег, вернуть клиентов, которые соответствуют обоим
            return Client.objects.filter(
                mobile_operator_code=self.mobile_operator_code,
                tag=self.tag
            )
        elif self.mobile_operator_code:
            # Если задан только код мобильного оператора, вернуть клиентов, которые соответствуют коду
            return Client.objects.filter(
                mobile_operator_code=self.mobile_operator_code
            )
        elif self.tag:
            # Если задан только тег, вернуть клиентов, которые соответствуют тегу
            return Client.objects.filter(tag=self.tag)
        # Если не задан код мобильного оператора и тег, вернуть всех клиентов
        return Client.objects.all()


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
