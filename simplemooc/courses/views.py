from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_name = 'courses/index.html'
    return render(request, template_name)