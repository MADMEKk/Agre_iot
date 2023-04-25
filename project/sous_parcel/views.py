from django.shortcuts import render,redirect
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
        # Start sending sensor data in a separate thread  
  
    if request.method == 'POST':
            data = json.loads(request.body)
            capterid = data.get('capterid', None) 
            sparcelid = data.get('sparcelid', None) 
            Thread(target=send_sensor_data,args=(capterid,sparcelid)).start()
            # Do something with the data
            return JsonResponse({'status': 'success'})
    else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
   
    # return render(request, 'sous_parcel/sparcel.html', {'sparcel': sparcelid})
@login_required
def S_parcel(request,id):
    sparcels =sous_parcel.objects.filter(parcel=id)
    return render(request,'sous_parcel/sparcels.html',{'sparcels':sparcels})

@login_required
def cree_s_parcel(request):
    if request.method == 'POST':
        form = creeSparceleForm(request.POST)

        if form.is_valid():
            new_sparcel = sous_parcel.objects.create(
                    user = User.objects.get(pk=request.user.id),
                    details = form.cleaned_data["details"],
                    name = form.cleaned_data["name"],
                )
            sous_parcel = new_sparcel.save()
            return redirect('sous_parcel/sparcels')
    else:
        form = creeSparceleForm()
    
    return render(request, 'sous_parcel/newsparcel.html', {'form': form})
@login_required
def sparcel(request,id):
    sparcel = sous_parcel.objects.get(pk=id)
    capters = capteur.objects.filter(sous_parcel=id)
    capters_list=list(capters.values())
    context ={'sparcel': sparcel,'capters_list':capters_list}
    return render(request, 'sous_parcel/sparcel.html',context )
@login_required
def capters_values(request,id):
    capters = capteur.objects.filter(sous_parcel=id)
    valeurs = []
    for cap in capters:
         
        valeur = valeur_capter.objects.filter(capteur=cap).values()[0:7]
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
def cree_capter(request):
    if request.method == 'POST':
        form = creeCApterForm(request.POST)

        if form.is_valid():
           
            capter = form.save()
            return redirect('sous_parcel/capters')
    else:
        form = creeCApterForm()
    
    return render(request, 'sous_parcel/newcapter.html', {'form': form})
