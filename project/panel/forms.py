from django.forms import ModelForm
from .models import parcel 
class CreeParcelForm(ModelForm):
    class Meta:
        model = parcel
        fields = ['name','details','location']