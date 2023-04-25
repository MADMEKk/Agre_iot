from django.forms import ModelForm
from .models import sous_parcel





class creeSparceleForm(ModelForm):
    class Meta:
        model = sous_parcel
        fields = ['name','details']

class creeCApterForm(ModelForm):
    class Meta:
        model = sous_parcel
        fields = '__all__'