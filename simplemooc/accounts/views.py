from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import RegisterForm

def register(request):
    templete_name = 'accounts/register.html'
    if request.method == 'POST':
        #form = UserCreationForm(request.POST) ***Aula Login inicial usando o forms padrão do user creation form***
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else: 
        #form = UserCreationForm() ***Aula Login inicial usando o forms padrão do user creation form***
        form = RegisterForm() # ** Form personalizado 
    context = { 
        'form': form
    }
    return render(request, templete_name, context)
