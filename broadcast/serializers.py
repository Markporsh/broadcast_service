from rest_framework import serializers
from broadcast.models import Client, Newsletter, Message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'phone_number', 'mobile_operator_code', 'tag']


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'start_date', 'message_text', 'mobile_operator_code', 'tag', 'end_date']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'created_date', 'newsletter', 'client']
        ordering = ['-created_date']
