"""myportfolio URL Configuration

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
from django.contrib import admin
from django.urls import path
from home.views import home
from myportfolio.views import base
from login.views import loginApp
from signup.views import signup
from django.conf import settings
from filters.views import filters,logoutApp,jobs
from django.conf.urls.static import static 

urlpatterns = [
    path('',home,name='home1'),
    path('admin/', admin.site.urls),
    path('base/',base,name='base'),
    path('home/',home,name='home'),
    path('login/',loginApp,name='login'),
    path('signup/',signup,name='signup'),
    path('filters/',filters,name='filters'),
    path('logoutApp/',logoutApp,name='logout'),
    path('jobs/',jobs,name='jobs')
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
