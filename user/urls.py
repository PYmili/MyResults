"""
URL configuration for MyResults project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import path

from user import views
from MyResults import settings

urlpatterns = [
    path('login/', views.login, name='login'),
    path('sgin_out/', views.sign_out, name='sign_out'),
    path('add_user/', views.add_user, name='add_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('toggle_publish_user/', views.toggle_publish_user, name='toggle_publish_user'),
    path('toggle_admin_user', views.toggle_admin_user, name='toggle_admin_user'),
]
