from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.stu_dash, name='stu_dash'),
    path('profile/', views.stu_profile, name='stu_profile')
]