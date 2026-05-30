from django.shortcuts import render, redirect
from datetime import date
from django.contrib import messages
from . import models
from student.models import Student, Application


def com_pending(request):
    return render(request, 'com_pending.html')


def com_profile(request):

    if request.method == 'POST':
        company_name = request.POST['company_name']
        hr_contact = request.POST['hr_contact']
        website = request.POST['website']
        company = models.Company.objects.get(user=request.user) 
        #request.user gives the user in session
        company.company_name = company_name
        company.hr_contact = hr_contact
        company.website = website
        company.save()  
        return redirect('com_pending')
    
    else:
        return render(request, 'com_profile.html')
    

def com_dash(request):
    company = models.Company.objects.get(user=request.user)
    ongoing_drives = models.Drive.objects.filter(company=company, completed=False)
    completed_drives = models.Drive.objects.filter(company=company, completed=True)

    drives = {
        'ongoing_drives': ongoing_drives,
        'completed_drives': completed_drives,
    }

    return render(request, 'com_dash.html', drives)


def create_drive(request):

    if request.method == 'POST':
        company = models.Company.objects.get(user=request.user)
        job_title = request.POST['job_title']
        job_description = request.POST['job_description']
        eligibility_criteria = request.POST['eligibility_criteria']
        location = request.POST['location']
        salary = request.POST['salary']
        application_deadline = request.POST['application_deadline']
        drive = models.Drive.objects.create(
            company = company,
            job_title = job_title,
            job_description = job_description,
            eligibility_criteria = eligibility_criteria,
            location = location,
            salary = salary,
            application_deadline = application_deadline,
        )
        return redirect('com_dash')
    
    else:
        return render(request, 'create_drive.html')
    

def company_details(request, company_id):
    company = models.Company.objects.get(id=company_id)
    ongoing_drives = models.Drive.objects.filter(company=company, completed=False)
    completed_drives = models.Drive.objects.filter(company=company, completed=True)

    context = {
        'company': company,
        'ongoing_drives': ongoing_drives,
        'completed_drives': completed_drives,
    }
    
    return render(request, 'company_details.html', context)


def drive_details(request, company_id, drive_id):
    company = models.Company.objects.get(id=company_id)
    drive = models.Drive.objects.get(id=drive_id)
    return render(request, 'drive_details.html', {'drive': drive, 'company': company})


def apply_drive(request, company_id, drive_id):

    if request.method == 'POST':
        student = Student.objects.get(user=request.user)
        drive = models.Drive.objects.get(id=drive_id)
        application = Application.objects.create(
            student=student,
            drive=drive,
            application_date=date.today(),
        )
        messages.success(request,'Application successful!')
        return redirect('drive_details' , company_id, drive_id)
    else:
        return redirect('drive_details' , company_id, drive_id)
    