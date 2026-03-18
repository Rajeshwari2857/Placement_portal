from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def student_dashboard(request):
    return render(request, 'student_dashboard.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def company_dashboard(request):
    return render(request, 'company_dashboard.html')
