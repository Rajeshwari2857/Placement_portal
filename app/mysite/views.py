from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def log_in(request):
    
    return render(request, 'log_in.html')


def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username=username).exists():
            messages.info("username already exists, try logging in")
        user = User.objects.create_user(
            email=request.POST['Email'],
            username=request.POST['Username'],
            password=request.POST['Password'],
            )  # this ['Username'] shud be the same as the 'name' in html file
        user.save()
        return redirect('stu_dash')
    else:
        return render(request, 'signup.html')
