from django.urls import path, include
from . import views  

urlpatterns = [
    path('', views.admin_dash, name='admin_panel'),
    path('dashboard/', views.admin_dash, name='admin_dash'),
    path('approval/', views.approved, name='approved'),
    path('blacklisted/', views.blacklisted, name='blacklisted'),
    path('pending/', views.com_pending, name='com_pending'),
]
