from django.urls import path
from broadcast.views import (
    ClientList, ClientDetail, NewsletterList, NewsletterDetail,
    MessageList, MessageDetail
)

app_name = 'broadcast'

urlpatterns = [
    path('clients/', ClientList.as_view(), name='client_list'),
    path('clients/<uuid:pk>/', ClientDetail.as_view(), name='client_detail'),
    path('newsletters/', NewsletterList.as_view(), name='newsletter_list'),
    path('newsletters/<uuid:pk>/', NewsletterDetail.as_view(), name='newsletter_detail'),
    path('messages/', MessageList.as_view(), name='message_list'),
    path('messages/<uuid:pk>/', MessageDetail.as_view(), name='message_detail'),
]
