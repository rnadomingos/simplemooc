#from django.urls import path, include
from . import views
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView


app_name='accounts'

urlpatterns = [
        url(r'^$', views.dashboard, name='dashboard'),
        url(r'^entrar/$', LoginView.as_view(), name='login'), 
        url(r'^cadastre-se/$', views.register, name='register'), 
        url(r'^sair/$', LogoutView.as_view(next_page='core:home'), name='logout'),
        url(r'^editar$', views.edit, name='edit'), 

]               