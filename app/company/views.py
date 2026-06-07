from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from student.models import Student, Application
from django.contrib.auth.decorators import login_required



def com_pending(request):
    return render(request, 'company/com_pending.html')

@login_required
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
        return render(request, 'company/com_profile.html')
    

def com_dash(request):
    company = models.Company.objects.get(user=request.user)
    ongoing_drives = models.Drive.objects.filter(company=company, completed=False)
    completed_drives = models.Drive.objects.filter(company=company, completed=True)

    drives = {
        'ongoing_drives': ongoing_drives,
        'completed_drives': completed_drives,
    }

    return render(request, 'company/com_dash.html', drives)


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
        return render(request, 'company/create_drive.html')
   

def complete_drive(request):
    if request.method == 'POST':
        drive_id = request.POST['drive_id']
        drive = models.Drive.objects.get(id=drive_id)
        drive.completed = True
        drive.save()
        return redirect('com_dash')
    else:
        return redirect('com_dash')


def review_drive(request, drive_id):
    drive = models.Drive.objects.get(id=drive_id, company__user=request.user)
    applications = Application.objects.filter(drive=drive, drive__user=request.user)

    context = {
        'applications': applications,
        'drive': drive,
    }
    return render(request, 'company/review_drive.html', context)


def student_application(request, drive_id, application_id):
    application = Application.objects.get(id=application_id)
    student = application.student
    drive = application.drive
    is_company = True

    context = {
        'application': application,
        'student': student,
        'drive': drive,
        'is_company': is_company,
    }
    return render(request, 'company/student_application.html', context)


def change_status(request, drive_id, application_id):
    
    # if request.method == 'POST':
    #     application = Application.objects.get(id=application_id)
    #     status = request.POST['status']

    #     if status == 'Shortlist':
    #         application.application_status = 'Shortlisted'
    #         application.save()
    #         return redirect('student_application', application_id)

    #     elif status == 'Accept':
    #         application.application_status = 'Accepted'
    #         application.save()
    #         return redirect('student_application', application_id)
        
    #     elif status == 'Reject':
    #         application.application_status = 'Rejected'
    #         application.save()
    #         return redirect('student_application', application_id)
        
    # else:
    #     return redirect('student_application', application_id)

    # this is ok, but an optimised solution would be:


    if request.method == 'POST':
        status =request.POST['status']
        status_map = {
            'Shortlist': 'Shortlisted',
            'Accept': 'Accepted',
            'Reject': 'Rejected',
        }

        application = Application.objects.get(id=application_id)
        application.application_status = status_map[status]
        application.save()
        return redirect('student_application',drive_id, application_id)
    else:
        return redirect('student_application',drive_id, application_id) 
    