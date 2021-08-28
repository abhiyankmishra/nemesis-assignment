"""nemesis_assignment URL Configuration

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
from . import Main_Data_Api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', Main_Data_Api.signupinterface),
    path('submitsignup', Main_Data_Api.submitsignupinterface),
    path('login/', Main_Data_Api.logininterface),
    path('checklogin', Main_Data_Api.checklogininterface),
    path('displayallusers/', Main_Data_Api.displayallusers),
    path('userdisplaybyusername/', Main_Data_Api.userdisplaybyusername),
    path('updatebyusername', Main_Data_Api.updatebyusername),
    path('userdeletebyusername/', Main_Data_Api.userdeletebyusername),
    path('logout/', Main_Data_Api.logout),






]
