from django.urls import path

from . import consumers
websocket_urlpatterns=[
    path('ws/<int:sparcel_id>/',consumers.sparcelconsumer.as_asgi()),
]
