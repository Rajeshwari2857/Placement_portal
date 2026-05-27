from django.shortcuts import render, redirect
from . import models


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
    return render(request, 'com_dash.html')


def create_drive(request):

    if request.method == 'POST':
        company = models.Company.objects.get(user=request.user)
        job_title = request.POST['job_title']
        job_description = request.POST['job_description']
        eligibility_criteria = request.POST['eligibility_criteria']
        application_deadline = request.POST['application_deadline']
        drive = models.Drive.objects.create(
            company = company,
            job_title = job_title,
            job_description = job_description,
            eligibility_criteria = eligibility_criteria,
            application_deadline = application_deadline,
        )
        return redirect('com_dash')
    
    else:
        return render(request, 'create_drive.html')
