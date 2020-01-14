"""d URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from d import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/',view.login,name='login'),
    path('loginIn/',view.loginIn,name='loginIn'),
    path('index/',view.index,name='index'),
    path('plan/',view.plan,name='plan'),
    path('stock/',view.Stock,name='stock'),
    path('gold/',view.gold,name='gold'),
    path('sunnyGirl/',view.sunnyGirl,name='sunnyGirl'),
    path('cle/',view.cle,name='cle'),
]
