from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.S_parcel,name='sparcels'),
    path('<int:id>/',views.sparcel,name='sparcel'),
    re_path('(?P<id>[\w-]+)/capters',views.capters,name='capters'),
]
