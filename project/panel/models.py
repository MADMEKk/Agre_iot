from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
class parcel(models.Model):
    
    name = models.CharField(max_length=255)
    details= models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.JSONField()
    def __str__(self):
        return self.name

class notification(models.Model):
    
    contenu = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    onclick=models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Profile(models.Model):   
    mobile =models.CharField(max_length=10)
    nakwa =models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agrecardid = models.CharField(max_length=500)
    image = models.ImageField(null=True,blank=True)  
