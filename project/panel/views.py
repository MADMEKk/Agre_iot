from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import parcel,Profile
from sous_parcel.models import sous_parcel ,capteur
from django.contrib.auth.models import User

def frontpage(request):
    current_user=request.user.id
    parcels =parcel.objects.filter(user_id=current_user)
    return render(request, 'panel/frontpage.html',{'parcels':parcels})

@login_required
def parcels(request):
    context =userinfo(request)
    return render(request,'panel/parcels.html',context)
@login_required
def userinfo(request):
    current_user=request.user.id
    parcels =parcel.objects.filter(user_id=current_user)
    sparcels =sous_parcel.objects.filter(parcel__in=parcels)
    sous_parcels=sparcels.count()
    capters =capteur.objects.filter(sous_parcel__in=sparcels).count()
    first_parcel =parcels.first()
    context ={'capters': capters,'sparcels':sous_parcels,'parcels':parcels,'first':first_parcel}
    return context

def profile(request):
    profil = request.user.profile
    return render(request,'panel/profile.html',{'user': request.user,'profile':profil})

