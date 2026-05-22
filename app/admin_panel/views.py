from django.shortcuts import render, redirect
from company.models import Company


def dashboard(request):

    pending = Company.objects.filter(approval_status='pending')
    approved = Company.objects.filter(approval_status='approved')
    blacklisted = Company.objects.filter(approval_status='blacklisted')
    companies = {
        'pending': pending, 
        'approved': approved,
        'blacklisted': blacklisted
        }
    return render(request, 'admin_dash.html', companies)


def approval(request):

    if request.method == 'POST':
        company_id = request.POST['company_id']
        company = Company.objects.get(id=company_id)
        company.approval_status = 'approved'
        company.save()
        return redirect('dashboard')
    
    else:
        return redirect('dashboard')


def blacklist(request):

    if request.method == 'POST':
        company_id = request.POST['company_id']
        company = Company.objects.get(id=company_id)
        company.approval_status = 'blacklisted'
        company.save()
        return redirect('dashboard')
    
    else:
        return redirect('dashboard')