from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='covid-homepage'),
    path('about', views.about, name='covid-about'),
]