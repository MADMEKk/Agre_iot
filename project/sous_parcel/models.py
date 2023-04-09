from django.db import models
from django.contrib.auth.models import User


class sous_parcel(models.Model):
    
    
    name = models.CharField(max_length=255)
    details= models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class capteur(models.Model):
    name = models.CharField(max_length=255)
    details= models.CharField(max_length=500)
    sous_parcel = models.ForeignKey(sous_parcel, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
