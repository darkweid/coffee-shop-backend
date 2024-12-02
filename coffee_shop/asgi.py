"""
ASGI config for coffee_shop project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from support.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffee_shop.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP запросы
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Ваши маршруты WebSocket
        )
    ),
})

