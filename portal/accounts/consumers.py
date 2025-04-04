from asgiref.sync import sync_to_async
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.task_id = self.scope["url_route"]["kwargs"]["task_id"]
        self.task_group_name = f"task_{self.task_id}"

        await self.channel_layer.group_add(self.task_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.task_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        user = self.scope["user"]

        # print(f"Получены данные: {data}")
        # print(f"Пользователь: {user}")

        if user:
            from django.contrib.auth.models import AnonymousUser

            if not isinstance(user, AnonymousUser) and user.is_authenticated:
                from .models import Comment

                try:
                    # print("Начало сохранения комментария...")
                    comment = await sync_to_async(Comment.objects.create)(
                        task_id=self.task_id, user=user, text=data["text"]
                    )
                    # print(f"Комментарий сохранен: {comment}")
                    await self.channel_layer.group_send(
                        self.task_group_name,
                        {
                            "type": "send_comment",
                            "user": user.username,
                            "text": comment.text,
                            "created_at": comment.created_at.strftime("%d.%m.%Y %H:%M"),
                        },
                    )
                except Exception as e:
                    # print(f"Ошибка при сохранении комментария: {e}")
                    await self.send(
                        text_data=json.dumps(
                            {"error": "Ошибка при добавлении комментария."}
                        )
                    )  # Отправляем ошибку клиенту.

    async def send_comment(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "user": event["user"],
                    "text": event["text"],
                    "created_at": event["created_at"],
                }
            )
        )
