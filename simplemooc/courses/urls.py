#from django.urls import path, include
from . import views
from django.conf.urls import url


app_name='courses'

urlpatterns = [
        #path('', views.home, name='home'),
        #path('contato/', views.contact, name='contact'),
        #path('', views.index, name='index#'),
        url(r'^$', views.index, name='index'), 
        #url(r'^(?P<pk>\d+)/$', views.details, name='details'),  #**modelo grupo (r'^(?P<pk>\d+)/$' **
        url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),

]