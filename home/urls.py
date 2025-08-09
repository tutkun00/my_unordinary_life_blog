from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name = 'home'),
    path('home', views.homePage, name = 'home'),
]