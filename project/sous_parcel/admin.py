from django.contrib import admin
from .models import sous_parcel,capteur,dispo_capteurs
# Register your models here.
admin.site.register(sous_parcel)
admin.site.register(capteur)
admin.site.register(dispo_capteurs)