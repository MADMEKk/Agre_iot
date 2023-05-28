from django.forms import ModelForm
from .models import parcel ,Profile
class CreeParcelForm(ModelForm):
    class Meta:
        model = parcel
        fields = ['name','details','location']
class CreeProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'