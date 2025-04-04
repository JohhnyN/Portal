from django.urls import path
from .consumers import CommentConsumer

websocket_urlpatterns = [
    path("ws/task/<int:task_id>/", CommentConsumer.as_asgi()),
]
