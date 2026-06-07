from django.urls import path, include
from . import views  

urlpatterns = [
    path('', views.admin_dash, name='admin_panel'),
    path('dashboard/', views.admin_dash, name='admin_dash'),
    path('approval/', views.approve_company, name='approve_company'),
    path('blacklisted/', views.blacklist_company, name='blacklist_company'),
    path('blacklist/', views.blacklist_student, name='blacklist_student'),
    path('complete_drive/', views.complete_drive, name='complete_drive'),
    path('dashboard/student_application/<int:application_id>/', views.adm_student_application, name='adm_student_application'),
    path('dashboard/drive_details/<int:company_id>/<int:drive_id>/', views.adm_drive_details, name='adm_drive_details'),
]
