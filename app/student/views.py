from django.shortcuts import render, redirect
from student import models


def stu_profile(request):

    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        graduation_year = request.POST['graduation_year']
        student = models.Student.objects.get(user=request.user) 
        #request.user gives the user in session
        student.name = name
        student.department = department
        student.graduation_year = graduation_year
        student.save()  
        return redirect('stu_dash')
    
    else:
        return render(request, 'stu_profile.html')
    
def stu_dash(request):
    return render(request, 'stu_dash.html')