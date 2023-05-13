from django.db import models
from django.contrib.auth.models import User
from panel.models import parcel
class sous_parcel(models.Model):
    
    name = models.CharField(max_length=255)
    details= models.CharField(max_length=500)     
    parcel = models.ForeignKey(parcel, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class dispo_capteurs(models.Model):
    name = models.CharField(max_length=255)
    details= models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class capteur(models.Model):
    name = models.CharField(max_length=255)
    details= models.CharField(max_length=500)
    sous_parcel = models.ForeignKey(sous_parcel, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    valeur_max = models.FloatField()
    valeur_min = models.FloatField()
    img = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class valeur_capter(models.Model):
    capteur = models.ForeignKey(capteur, related_name='value', on_delete=models.CASCADE)
    content = models.FloatField()
    voltage=models.FloatField()
    température=models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ('date_added',)
