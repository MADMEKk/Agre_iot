from django.urls import path,re_path
from . import views
app_name = 'sous_parcel'
urlpatterns = [
    path('<int:id>/',views.S_parcel,name='sparcels'),
    path('sparcel/<int:id>/',views.sparcel,name='sparcel'),
    re_path('(?P<id>[\w-]+)/capters',views.capters,name='capters'),
    path('capter/run',views.run_capter,name='runcapter'),
    path('capters/valeurs',views.capters_values,name='capter_value'),
    path('creatcapter/<int:sparcelid>/',views.cree_capter,name='cree_capter'),
]

