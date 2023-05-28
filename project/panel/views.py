from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import parcel,notification,Profile
from sous_parcel.models import sous_parcel ,capteur
from django.contrib.auth.models import User
from .forms import CreeParcelForm ,CreeProfileForm
from django.http import JsonResponse
import json
def tables(request):
    current_user=request.user.id
    parcels =parcel.objects.filter(user_id=current_user)
    sparcels =sous_parcel.objects.filter(parcel__in=parcels)
    capters =capteur.objects.filter(sous_parcel__in=sparcels)
    first_parcel =parcels.first()
    context ={'capters': capters,'sparcels':sparcels,'parcels':parcels,'first':first_parcel}
    return render(request,'panel/tables.html',context)
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
    pr = request.user.id
    if(Profile.objects.filter(user=pr).count() >=1):
        profil = request.user.profile
        return render(request,'panel/profile.html',{'user': request.user,'profile':profil})
    else : 
        return redirect('panel:cree_profile')

@login_required
@method_decorator(csrf_exempt, name='dispatch')
def cree_parcel(request):
    if request.method == 'POST':
        form = CreeParcelForm(request.POST)
        if form.is_valid():
            new_parcel = parcel(
                        user = request.user,
                        details = form.cleaned_data["details"],
                        name = form.cleaned_data["name"],
                        location = form.cleaned_data["location"],
                    )
            new_parcel.save()
            context = {'status': 'success'}
            return JsonResponse({'status': 'succes'})

        else:  return JsonResponse({'status': 'failed'})
    else : 
        form = CreeParcelForm()
    return render(request,'panel/newparcel.html',{'form':form})

@login_required
@method_decorator(csrf_exempt, name='dispatch')
def cree_profile(request):
    user = request.user.profile
    if request.method == 'POST':
        form = CreeProfileForm(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
            context = {'status': 'success'}
            return JsonResponse(context)

        else:  return JsonResponse({'status': 'failed'})
    else : 
        form = CreeProfileForm(instance=user)
    return render(request,'panel/creeprofile.html',{'form':form})


@login_required
@method_decorator(csrf_exempt, name='dispatch')
def notifications(request):
        valeurs = []
        valeur = notification.objects.filter(user=request.user.id).values().order_by('-id')[:4]
        val = list(valeur)
        valeurs += val
        return JsonResponse({'valeurs': valeurs})