from django.urls import path
from . import views


urlpatterns = [
    path('', views.showAllPosts, name = 'blog'),
    path('migrate/', views.migrate_view),
    path('<slug:slug>/', views.showPost),
] 
