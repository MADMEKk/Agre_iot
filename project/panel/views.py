from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import parcel

def frontpage(request):
    return render(request, 'panel/frontpage.html')

@login_required
def parcels(request):
    current_user=request.user.id
    parcels =parcel.objects.filter(user_id=current_user)
    return render(request,'panel/parcels.html',{'parcels':parcels})
