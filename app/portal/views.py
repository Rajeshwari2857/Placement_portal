from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'krishiv'})


def login(request):
    return render(request, 'login.html', {'name': 'krishiv'})


def signup(request):
    return render(request, 'signup.html', {'name': 'krishiv'})
