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

from achievement import views
from MyResults import settings

urlpatterns = [
    path('add_achievement/', views.add_achievement, name='add_achievement'),
    path('delete_achievement/', views.delete_achievement, name='delete_achievement'),
    path('toggle_publish_achievement/', views.toggle_publish_achievement, name='toggle_publish_achievement'),
    path('add_category/', views.add_category, name='add_category'),
    path('delete_category', views.delete_category, name='delete_category'),
]
