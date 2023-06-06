from django.forms import ModelForm
from .models import sous_parcel, capteur
from panel.models import parcel 


        
class creeCApterForm(ModelForm):
    
    class Meta:
        model = capteur
        fields = ['name','details','latitude','longitude','valeur_max','valeur_min','img']