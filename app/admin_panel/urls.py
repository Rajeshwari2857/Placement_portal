from django.urls import path, include
from . import views  

urlpatterns = [
    path('', views.dashboard, name='admin_panel'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('approval/', views.approved, name='approved'),
    path('blacklisted/', views.blacklisted, name='blacklisted'),
    path('pending/', views.pending, name='pending'),
]
