"""simplemooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path, include
#from simplemooc.core import urls, views
#from simplemooc.courses import urls, views

from django.contrib import admin
from django.urls import path, include
from simplemooc.core import views, urls
from simplemooc.courses import views, urls
from django.conf import settings
#from django.conf.urls.static import static



#urlpatterns = [
#        path('', include(urls,namespace='core')),
#        path('cursos/', include(urls,namespace='courses')),
#        path('admin/', admin.site.urls),
#]

urlpatterns = [
	path('', include('simplemooc.core.urls', namespace='Core')),
    path('cursos/', include('simplemooc.courses.urls', namespace='Courses')),
  #  path('conta/', include('simplemooc.accounts.urls', namespace='Accounts')),
  #  path('forum/', include('simplemooc.forum.urls', namespace='Forum')),
	
    path('admin/', admin.site.urls),
] 
