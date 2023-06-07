from django.forms import ModelForm
from .models import parcel ,Profile
from sous_parcel.models import sous_parcel
class CreeParcelForm(ModelForm):
    class Meta:
        model = parcel
        fields = ['name','details','location']
class CreeProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile','agrecardid','image']
class creeSparceleForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(creeSparceleForm, self).__init__(*args, **kwargs)
        self.fields['parcel'].queryset = parcel.objects.filter(user=user)
    class Meta:
        model = sous_parcel
        fields = '__all__'