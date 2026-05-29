from django.shortcuts import render, redirect
from student.models import Student, Application
from company.models import Company, Drive

def stu_profile(request):

    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        graduation_year = request.POST['graduation_year']
        student = Student.objects.get(user=request.user) 
        resume = request.FILES.get('resume')

        student.name = name
        student.department = department
        student.graduation_year = graduation_year
        student.resume = resume
        student.save()  
        return redirect('stu_dash')
    
    else:
        return render(request, 'stu_profile.html')
    

def stu_dash(request):

    available_drives = Drive.objects.filter(completed=False)
    companies = Company.objects.filter(approval_status='Approved')
    student = Student.objects.get(user=request.user)
    applied_drives = Application.objects.filter(student=student, application_status='Applied')

    context = {
        'available_drives': available_drives,
        'companies': companies,
        'applied_drives': applied_drives,
    }
    return render(request, 'stu_dash.html', context)