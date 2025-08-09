from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name = 'home'),
    path('migrate/', views.migrate_view),
    path('home', views.homePage, name = 'home'),
]