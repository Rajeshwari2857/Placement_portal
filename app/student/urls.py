from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.stu_dash, name='stu_dash'),
    path('profile/', views.stu_profile, name='stu_profile'), 
    path('dashboard/company/<int:company_id>/', views.company_details, name='company_details'), 
    path('dashboard/company/<int:company_id>/drive/<int:drive_id>/', views.stu_drive_details, name='stu_drive_details'), 
    path('dashboard/company/<int:company_id>/drive/<int:drive_id>/apply/', views.apply_drive, name='apply_drive'), 
    path('dashboard/application/<int:application_id>/', views.application_details, name='application_details'), 
    path('dashboard/application_history/<int:student_id>/', views.application_history, name='application_history'),
]
