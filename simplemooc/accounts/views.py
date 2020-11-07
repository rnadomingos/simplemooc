from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import RegisterForm, EditAccountForm


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)

def register(request):
    templete_name = 'accounts/register.html'
    if request.method == 'POST':
        #form = UserCreationForm(request.POST) ***Aula Login inicial usando o forms padrão do user creation form***
        form = RegisterForm(request.POST)
        if form.is_valid():
            #form.save()
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
                )
            login(request, user)
            return redirect('core:home')
            return redirect(settings.LOGIN_URL)
    else: 
        #form = UserCreationForm() ***Aula Login inicial usando o forms padrão do user creation form***
        form = RegisterForm() # ** Form personalizado 
    context = { 
        'form': form
    }
    return render(request, templete_name, context)


@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    form = EditAccountForm()
    context = {}
    context['form'] = form
    return render(request, template_name, context)