from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
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
    applied_drives = Application.objects.filter(student=student)

    context = {
        'available_drives': available_drives,
        'companies': companies,
        'applied_drives': applied_drives,
    }
    return render(request, 'stu_dash.html', context)


def company_details(request, company_id):
    company = Company.objects.get(id=company_id)
    ongoing_drives = Drive.objects.filter(company=company, completed=False)
    completed_drives = Drive.objects.filter(company=company, completed=True)

    context = {
        'company': company,
        'ongoing_drives': ongoing_drives,
        'completed_drives': completed_drives,
    }
    
    return render(request, 'company_details.html', context)


def drive_details(request, company_id, drive_id):
    company = Company.objects.get(id=company_id)
    drive = Drive.objects.get(id=drive_id)
    return render(request, 'drive_details.html', {'drive': drive, 'company': company})


def apply_drive(request, company_id, drive_id):

    if request.method == 'POST':
        student = Student.objects.get(user=request.user)
        drive = Drive.objects.get(id=drive_id)
        
        if Application.objects.filter(student=student, drive=drive).exists():
            messages.error(request,'You have already applied to this drive.')
            return redirect('drive_details', company_id, drive_id)
        
        else: 
            application = Application.objects.create(
                student=student,
                drive=drive,
                application_date=date.today(),
            )
            messages.success(request,'Application successful!')
            return redirect('drive_details' , company_id, drive_id)
    else:
        return redirect('drive_details' , company_id, drive_id)
    
def application_details(request, application_id):
    application = Application.objects.get(id=application_id)
    return render(request, 'application_details.html', {'application': application})