from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from student.models import Student
from company.models import Company



def log_in(request):

    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        role = request.POST['role']

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username not found")
            return redirect('log_in')
        
        else:
            user = authenticate(username=username, password=password)
            #returns user w credentials or NONE if not found
            if user is None:
                messages.error(request, "Wrong password, try again")
                return redirect('log_in')
            
            else:
                if role == 'Student':
                    login(request, user)
                    return redirect('stu_dash')
                
                elif user.is_superuser:
                    login(request, user)
                    return redirect('admin_panel')
                
                else:
                    login(request, user)
                    company = Company.objects.get(user=user)
                    if company.approval_status == 'Approved':
                        return redirect('com_dash')
                    elif company.approval_status == 'Pending':
                        return redirect('com_pending')
                    else:
                        messages.error(request, 'Your company has been blacklisted')
                        return redirect('log_in')
                    
            #checked user existence first cuz authenticate returns NONE for WRONG PASSWORD and NO USER FOUND
                            
    else:
        return render(request, 'log_in.html')


def signup(request):

    if request.method == 'POST':
        email = request.POST['Email']
        username = request.POST['Username']
        password = request.POST['Password']
        role = request.POST['role']
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
            if role == 'Student':
                Student.objects.create(user=user)
                login(request, user)
                return redirect('stu_dash')
            else:
                Company.objects.create(user=user)
                login(request, user)
                return redirect('com_profile')
    else:
        return render(request, 'signup.html')       
