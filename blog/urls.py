from django.urls import path
from . import views


urlpatterns = [
    path('', views.showAllPosts, name = 'blog'),
    path('<slug:slug>/', views.showPost),
] 
