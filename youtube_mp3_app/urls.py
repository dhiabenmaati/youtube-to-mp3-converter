from django.contrib import admin
from django.urls import path
from youtube_mp3_app import views



urlpatterns = [
    path('', views.index, name='home'),
    path('get-link', views.getLink, name='get-link-api'),
]

