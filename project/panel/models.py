from django.db import models
from django.contrib.auth.models import User

class parcel(models.Model):
    
    name = models.CharField(max_length=255)
    details= models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
