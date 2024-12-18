"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomToken
router = DefaultRouter()
router.register('studentapi',views.StudentClass,basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    #path('gettoken/',obtain_auth_token), # will verify token inputed by user as name & pass based. 
    #path('gettoken/',CustomToken.as_view()) # custom token , 
]

'''
admin based token Generated!
drf_create_token cmd based token Generated!
Exposing API endpoint based by cmd as above obtain_auth_token url after token Generated!
Using Signals based token Generated!, Means when someone create username nd pass then 
automatcically token ll be generated! see in models for details. also we not need to manuplate the url in this case
'''