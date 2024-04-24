"""
URL configuration for onlyflans_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
# from static_pages.views import indice, acerca, bienvenido, contacto, exito, registrate
from static_pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indice, name='indice'),
    path('acerca/', views.acerca, name='acerca'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
    path('registrate/', views.registro, name='registrate'),
    path('registration/', include('django.contrib.auth.urls')),
]
