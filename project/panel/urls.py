from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "panel"
urlpatterns = [
path('', views.frontpage, name='frontpage'),
path('parcels/',views.parcels,name='parcels'),
path('creatparcel/',views.cree_parcel,name='cree_parcel'),
path('creatprofile/',views.cree_profile,name='cree_profile'),
path('notifications/',views.notifications,name='notifications'),
path('profile/',views.profile,name='profile'),
path('tables/',views.tables,name='tables')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)