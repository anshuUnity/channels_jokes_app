"""
ASGI config for channel_joke project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.urls import path

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ProtocolTypeRouter

from joke.consumers import GetJokeConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channel_joke.settings')

application = get_asgi_application()

wspatterns = [
    path('ws/joke/', GetJokeConsumer),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            wspatterns
        )
    )
})
