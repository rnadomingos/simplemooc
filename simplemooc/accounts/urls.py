#from django.urls import path, include
from . import views
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView


app_name='accounts'

urlpatterns = [
        url(r'^entrar/$', LoginView.as_view(), name='login'), 

]