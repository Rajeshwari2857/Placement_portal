from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


def log_in(request):

    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username not found, sign up")
            return redirect('signup')
        
        else:
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Wrong password, try again")
                return redirect('log_in')
            
            else:
                login(request, user)
                return redirect('stu_dash')
                            
    else:
        return render(request, 'log_in.html')


def signup(request):

    if request.method == 'POST':
        email = request.POST['Email']
        username = request.POST['Username']
        password = request.POST['Password']
        # this ['Username'] shud be the same as the 'name' in html file
    
        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists, try logging in")
            return redirect('log_in')
        
        elif User.objects.filter(email=email).exists():
            messages.error(request, "email already exists, try logging in")
            return redirect('log_in')
        
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password)
            login(request, user)
            return redirect('stu_dash')
    else:
        return render(request, 'signup.html')
