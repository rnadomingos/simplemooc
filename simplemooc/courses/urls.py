#from django.urls import path, include
from . import views
from django.conf.urls import url


app_name='courses'

urlpatterns = [
        #path('', views.home, name='home'),
       #path('contato/', views.contact, name='contact'),
        url(r'^$', views.index, name='index'), 
        #path('', views.index, name='index#'),

]