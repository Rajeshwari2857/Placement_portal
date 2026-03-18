from django.urls import path, include

from . import views  

urlpatterns = [
    path('', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('dashboard/student/', views.student_dashboard, name="student_dashboard"),
    path('dashboard/admin/', views.admin_dashboard, name="admin_dashboard"),
    path('dashboard/company/', views.company_dashboard, name="company_dashboard"),
]