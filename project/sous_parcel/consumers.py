import json
from asgiref.sync import async_to_sync
from .models import *
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.serializers import serialize
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
        
    async def receive(self):
         pass
   
    async def sensor_data(self, event):
        # Send the sensor data to all connected clients
        capterid = event['capterid']
        value = event['value']
        sparcelid = event['sparcel']
        captername = event['captername']
        température = event['température']
        voltage = event['voltage']
        await self.send(text_data=json.dumps({
             'value': value,
              'sparcel': sparcelid,
              'capterid' : capterid,
              'voltage':voltage,
              'température':température,
              'captername' : captername
        }))

#user notification channel 
class Userconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name= 'user_%d' % user_id
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
        
    async def receive(self):
         pass
   
    async def notification(self, event):
        # Send the sensor data to all connected clients
        value = event['value']
        sparcel = event['sparcel']
        captername = event['captername']
        await self.send(text_data=json.dumps({
             'value': value,
             'sparcel':sparcel,
             'captername' : captername
        }))



def send_sensor_data(capter_id,sparcel_id,user_id):
         
            import time
            import random
            from channels.layers import get_channel_layer
            from django.utils import timezone           
             # Get the channel layer
            channel_layer = get_channel_layer()
            max= capteur.objects.filter(pk=capter_id).values('valeur_max')
            min= capteur.objects.filter(pk=capter_id).values('valeur_min')
            val_max = float(max[0]['valeur_max'])
            val_min = float(min[0]['valeur_min'])
            group_name= 'sparcel_%d' % sparcel_id
            while True:
                # Generate some fake sensor data
                capter= capteur.objects.get(pk=capter_id)
                value = round(random.randint(29.0, 40.0), 2)
                température = round(random.randint(10.0, 60.0), 2)
                voltage = round(random.randint(20.0, 30.0), 2)
                if(value>=val_max or value <= val_min):
                   
                    
                    user_group_name= 'user_%d' % user_id
                    async_to_sync(channel_layer.group_send)(
                    user_group_name, 
                    {'type': 'notification',
                     'value': value,
                     'sparcel':sparcel_id,
                    'captername' : capter.name
                    }
                    )
                        
                from datetime import timezone

                
                # Save the sensor data to the database
                capter_data = valeur_capter(capteur=capteur(id=capter_id), content=value,voltage=voltage,température=température)
               
                capter_data.save()
                # Send the sensor data to all connected clients via WebSocket
                async_to_sync(channel_layer.group_send)(
                    group_name, 
                    {'type': 'sensor_data',
                     'value': value,
                    'sparcel': sparcel_id,
                    'capterid' : capter_id,
                    'voltage':voltage,
                    'température':température,
                    'captername' : capter.name
                    }
                    )

                # Wait for a few seconds before sending more data
                time.sleep(5)













 