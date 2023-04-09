import json
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
class sparcelconsumer():
    async def connect(self):
        self.sparcel_id = self.scope['url_route']['kwargs']['sparcel_id']
        self.sparcel_group_name= 'sparcel_%s' % self.sparcel_id
        await self.channel_layer.group_add(
            self.sparcel_group_name,
            self.channel_name
        )

        await self.accept()
    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.sparcel_group_name,
            self.channel_name
        )