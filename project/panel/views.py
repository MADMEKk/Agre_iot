from django.shortcuts import render , redirect


def frontpage(request):
    return render(request, 'panel/frontpage.html')

