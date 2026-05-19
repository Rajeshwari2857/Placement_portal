from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.stu_dash, name='stu_dash')
]