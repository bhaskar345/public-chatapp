from django.urls import path

from app.consumers import Chatconsumer

websocket_urlpatterns = [
    path('chat/<str:user>/', Chatconsumer.as_asgi()),
]