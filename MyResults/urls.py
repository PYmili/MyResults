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
from django.urls import path, include

import user.views as user_views
import home.views as home_views
import control.views as control_views
from MyResults import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('user/', include('user.urls'), name='user'),
    path('control/', control_views.control, name='control'),
    path('achievement/', include('achievement.urls'), name='achievement'),
    path('news/', include('news.urls'), name='news'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
