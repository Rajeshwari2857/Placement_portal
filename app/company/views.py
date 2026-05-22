from django.shortcuts import render, redirect
from . import models


def pending(request):
    return render(request, 'pending.html')


def profile(request):

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
        return redirect('pending')
    
    else:
        return render(request, 'profile.html')
    
def comp_dash(request):
    return render(request, 'comp_dash.html')