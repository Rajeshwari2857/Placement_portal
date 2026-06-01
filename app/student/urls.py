from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.stu_dash, name='stu_dash'),
    path('profile/', views.stu_profile, name='stu_profile'), 
    path('dashboard/<int:company_id>/', views.company_details, name='company_details'), 
    path('dashboard/<int:company_id>/<int:drive_id>/', views.drive_details, name='drive_details'), 
    path('dashboard/<int:company_id>/<int:drive_id>/', views.apply_drive, name='apply_drive'), 
    path('dashboard/application/<int:application_id>/', views.application_details, name='application_details'), 
]
