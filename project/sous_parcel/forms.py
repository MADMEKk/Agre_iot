from django.forms import ModelForm
from .models import sous_parcel, capteur
from panel.models import parcel 


        
class creeCApterForm(ModelForm):
    def __init__(self, prcl, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sous_parcel'].queryset =  sous_parcel.objects.filter(parcel=prcl)
    class Meta:
        model = capteur
        fields = '__all__'