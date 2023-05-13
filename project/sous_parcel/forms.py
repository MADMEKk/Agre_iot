from django.forms import ModelForm
from .models import sous_parcel, capteur
from panel.models import parcel 

class creeSparceleForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(creeSparceleForm, self).__init__(*args, **kwargs)
        self.fields['parcel'].queryset = parcel.objects.filter(user=user)

    class Meta:
        model = sous_parcel
        fields = '__all__'
        
class creeCApterForm(ModelForm):
    def __init__(self, prcl, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sous_parcel'].queryset =  sous_parcel.objects.filter(parcel=prcl)


    class Meta:
        model = capteur
        fields = '__all__'