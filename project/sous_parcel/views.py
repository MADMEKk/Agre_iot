from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import creeSparceleForm,creeCApterForm
from .models import *
from panel.models import parcel
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from threading import Thread
from .consumers import send_sensor_data
import json
@method_decorator(csrf_exempt, name='dispatch')
def run_capter(request):

    if request.method == 'POST':
            data = json.loads(request.body)
            capterid = data.get('capterid', None) 
            sparcelid = data.get('sparcelid', None) 
            Thread(target=send_sensor_data,args=(capterid,sparcelid,request.user.id)).start()
            return JsonResponse({'status': 'success'})
    else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
   
    # return render(request, 'sous_parcel/sparcel.html', {'sparcel': sparcelid})
@login_required
def S_parcel(request,id):
    sparcels =sous_parcel.objects.filter(parcel=id)
    first_sparcel =sparcels.first()
    return render(request,'sous_parcel/sparcels.html',{'sparcels':sparcels,'first':first_sparcel})

@login_required
@method_decorator(csrf_exempt, name='dispatch')
def cree_s_parcel(request):
    if request.method == 'POST':
        form = creeSparceleForm(request.user,request.POST)

        if form.is_valid():
            new_sparcel = sous_parcel.objects.create(
                    parcel = form.cleaned_data["parcel"],
                    details = form.cleaned_data["details"],
                    name = form.cleaned_data["name"],
                )
            new_sparcel.save()
            return JsonResponse({'status': 'success'})
        else:  return JsonResponse({'status': 'failed'})
    else:
        form = creeSparceleForm(request.user)
    
    return render(request, 'sous_parcel/newsparcel.html', {'form': form})
@login_required
def sparcel(request,id):
    sparcel = sous_parcel.objects.get(pk=id)
    parcele= parcel.objects.get(pk=sparcel.parcel_id)
    capters = capteur.objects.filter(sous_parcel=id)
    capters_list=list(capters.values())
    context ={'sparcel': sparcel,'capters_list':capters_list,'parcel':parcele}
    return render(request, 'sous_parcel/sparcel.html',context )
@login_required
@method_decorator(csrf_exempt, name='dispatch')
def capters_values(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cap = data.get('capterid', None) 
        valeurs = []
        valeur = valeur_capter.objects.filter(capteur_id=cap).values().order_by('-id')[:7]
        val = list(valeur)
        valeurs += val
        return JsonResponse({'valeurs': valeurs})

@login_required
def capters(request,id):
    sparcel = sous_parcel.objects.get(pk=id)
    capters = capteur.objects.filter(sous_parcel=id)
    context ={'capters': capters,'sparcel':sparcel} 
    return render(request, 'sous_parcel/capters.html', context)

@login_required
@method_decorator(csrf_exempt, name='dispatch')
def cree_capter(request,sparcelid):
    if request.method == 'POST':
        form = creeCApterForm(sparcelid,request.POST or None)
        if form.is_valid():
            new_capter = capteur(
                        details = form.cleaned_data["details"],
                        name = form.cleaned_data["name"],
                        img = form.cleaned_data["img"],
                        longitude = form.cleaned_data["longitude"],
                        latitude = form.cleaned_data["latitude"],
                        sous_parcel = form.cleaned_data["sous_parcel"],
                    )
            new_capter.save()
            context = {'status': 'success'}
            return redirect('sous_parcel:sparcel',sparcelid)

        else:  return JsonResponse({'status': 'failed'})
    else:
        form = creeCApterForm(sparcelid)
        dispocapter = dispo_capteurs.objects.all()
        sparcel=sous_parcel.objects.filter(pk=sparcelid).values('parcel')[0]
        parcel_loc=parcel.objects.filter(pk=sparcel.get('parcel')).values('location')[0]
        return render(request, 'sous_parcel/newcapter.html', {'form': form,'dispo':dispocapter,'parcel_loc':parcel_loc})

