from django.urls import path, include
from . import views  

urlpatterns = [
    path('pending/', views.com_pending, name='com_pending'),
    path('profile/', views.com_profile, name='com_profile'), 
    path('dashboard/', views.com_dash, name='com_dash'), 
    path('dashboard/complete_drive/', views.complete_drive, name='complete_drive'),
    path('dashboard/create_drive/', views.create_drive, name='create_drive'),
    path('dashboard/review_drive/<int:drive_id>/', views.review_drive, name='review_drive'),
    path('dashboard/review_drive/<int:drive_id>/<int:application_id>/', views.student_application, name='student_application'),
    path('dashboard/review_drive/<int:drive_id>/<int:application_id>/change_status/', views.change_status, name='change_status'),
]
