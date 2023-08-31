"""
URL configuration for youtubemusic project.

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
from django.urls import path
from django.urls import path
from youtubemusic.views import down_song
from youtubemusic.views import get_info
from youtubemusic.views import getPlay
from youtubemusic.views import searchsong
from youtubemusic.views import getHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('downs/', down_song, name='down_song'),
    path('getinfo/', get_info, name='get_info'),
    path('downlist/', down_song, name='down_song'),
    path('getplay/', getPlay, name='getPlay'),
    path('search/', searchsong, name='searchsong'),
    path('getHome/', getHome, name='getHome'),
]
