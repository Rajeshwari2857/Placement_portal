from django.urls import path, include
from . import views
from company.views import apply_drive

urlpatterns = [
    path('dashboard/', views.stu_dash, name='stu_dash'),
    path('profile/', views.stu_profile, name='stu_profile'),
    path('<int:company_id>/<int:drive_id>/', apply_drive, name='apply_drive'), 
    path('application/<int:application_id>/', views.application_details, name='application_details'), 
]
