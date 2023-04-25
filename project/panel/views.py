from django.shortcuts import render , redirect


def frontpage(request):
    return render(request, 'panel/frontpage.html')

@login_required
def parcels(request):
    current_user=request.user.id
    parcels =parcel.objects.filter(user_id=current_user)
    return render(request,'panel/parcels.html',{'parcels':parcels})
