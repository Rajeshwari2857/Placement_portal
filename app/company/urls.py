from django.urls import path, include
from . import views  

urlpatterns = [
    path('pending/', views.com_pending, name='com_pending'),
    path('profile/', views.com_profile, name='com_profile'), 
    path('dashboard/', views.com_dash, name='com_dash'), 
]
