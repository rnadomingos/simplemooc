from django.urls import path, include
from . import views

app_name='courses'

urlpatterns = [
        #path('', views.home, name='home'),
        #path('contato/', views.contact, name='contact'),
        path('', views.index, name='index'),

]