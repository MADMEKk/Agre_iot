from django.shortcuts import render,redirect
from .forms import creeSparceleForm,creeCApterForm
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def S_parcel(request):
    current_user=request.user.id
    sparcels =sous_parcel.objects.filter(user_id=current_user)
    return render(request,'sous_parcel/sparcels.html',{'sparcels':sparcels})

@login_required
def cree_s_parcel(request):
    if request.method == 'POST':
        form = creeSparceleForm(request.POST)

        if form.is_valid():
            new_sparcel = sous_parcel.objects.create(
                    user = User.objects.get(pk=request.user.id),
                    details = form.cleaned_data["details"],
                    slug = form.cleaned_data["slug"],
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
    return render(request, 'sous_parcel/sparcel.html', {'sparcel': sparcel})
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
