from django.urls import path

from . import views
app_name = "panel"
urlpatterns = [
path('', views.frontpage, name='frontpage'),
path('parcels/',views.parcels,name='parcels'),
path('profile/',views.profile,name='profile')

]