import json
from asgiref.sync import async_to_sync
from .models import *
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
class sparcelconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        sparcel_id = self.scope['url_route']['kwargs']['sparcel_id']
        self.room_group_name= 'sparcel_%d' % sparcel_id
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
         pass
    #    data = json.loads(text_data)
    #    capterid = data['id']
    #    value = data['value']
    #    sparcelid = data['sparcel']
    #    await self.channel_layer.group_send(
    #        self.room_group_name,
    #        {
    #            'type': 'chat_message',
    #           'value': value,
    #           'sparcel': sparcelid,
    #           'capterid' : capterid
    #        }
    #    )
    
    # async def chat_message(self, event):
    #     capterid = event['capterid']
    #     value = event['value']
    #     sparcelid = event['sparcel']
    #     await self.send(text_data=json.dumps({
    #          'value': value,
    #           'sparcel': sparcelid,
    #           'capterid' : capterid
    #     }))
    async def sensor_data(self, event):
        # Send the sensor data to all connected clients
        capterid = event['capterid']
        value = event['value']
        sparcelid = event['sparcel']
        captername = event['captername']
        await self.send(text_data=json.dumps({
             'value': value,
              'sparcel': sparcelid,
              'capterid' : capterid,
              'captername' : captername
        }))

def send_sensor_data(capter_id,sparcel_id):
            """
            This function simulates sending sensor data to the web app.
            In a real-world scenario, this function would read sensor data
            from a physical device.
            """
            import time
            import random
            from channels.layers import get_channel_layer

            # Get the channel layer
            channel_layer = get_channel_layer()


            group_name= 'sparcel_%d' % sparcel_id
            while True:
                # Generate some fake sensor data
                
                value = round(random.randint(20.0, 30.0), 2)
               
                
                from datetime import timezone

                
                # Save the sensor data to the database
                capter_data = valeur_capter(capteur=capteur(id=capter_id), content=value)
               
                capter_data.save()
                # Send the sensor data to all connected clients via WebSocket
                capter= capteur.objects.get(pk=capter_id)
                async_to_sync(channel_layer.group_send)(
                    group_name, 
                    {'type': 'sensor_data',
                     'value': value,
                    'sparcel': sparcel_id,
                    'capterid' : capter_id,
                    'captername' : capter.name
                    }
                    )

                # Wait for a few seconds before sending more data
                time.sleep(5)












 