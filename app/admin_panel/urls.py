from django.urls import path, include
from . import views  

urlpatterns = [
    path('', views.admin_dash, name='admin_panel'),
    path('dashboard/', views.admin_dash, name='admin_dash'),
    path('approval/', views.approve_company, name='approve_company'),
    path('blacklisted/', views.blacklist_company, name='blacklist_company'),
    path('blacklist/', views.blacklist_student, name='blacklist_student'),
    path('complete_drive/', views.complete_drive, name='complete_drive'),
]
