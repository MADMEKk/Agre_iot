from django.shortcuts import render

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: not u.is_authenticated, login_url='panel:frontpage')
def frontpage(request):
    return render(request, 'core/frontpage.html')
@user_passes_test(lambda u: not u.is_authenticated, login_url='panel:frontpage')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('panel:frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})