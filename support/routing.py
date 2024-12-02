from django.urls import path
from .consumers import SupportChatConsumer

websocket_urlpatterns = [
    path('ws/support/', SupportChatConsumer.as_asgi()),
]
