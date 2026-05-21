from django.urls import path, include
from . import views  

urlpatterns = [
    path('pending/', views.pending, name='pending'),
    path('profile/', views.profile, name='profile'), 
]
