"""
URL configuration for DRF_PostgreSQL_React project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    re_path(r"^department$", department, name='department'),
    re_path(r"^department/([0-9]+)$", department, name='department'),
    path('api1/', CarAPIList.as_view()),

    path('employee', employeeApi, name='department'),
    path('employee/<int:id>', employeeApi, name='department'),

    re_path(r'^employee/savefile', SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)