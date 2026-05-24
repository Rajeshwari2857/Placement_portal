from django.shortcuts import render, redirect
from company.models import Company


def admin_dash(request):

    pending = Company.objects.filter(approval_status='Pending')
    approved = Company.objects.filter(approval_status='Approved')
    blacklisted = Company.objects.filter(approval_status='Blacklisted')
    companies = {
        'pending': pending, 
        'approved': approved,
        'blacklisted': blacklisted
        }
    return render(request, 'admin_dash.html', companies)


def approved(request):

    if request.method == 'POST':
        company_id = request.POST['company_id']
        company = Company.objects.get(id=company_id)
        company.approval_status = 'Approved'
        company.save()
        return redirect('admin_dash')
    
    else:
        return redirect('admin_dash')


def com_pending(request):

    if request.method == 'POST':
        company_id = request.POST['company_id']
        company = Company.objects.get(id=company_id)
        company.approval_status = 'Pending'
        company.save()
        return redirect('admin_dash')
    
    else:
        return redirect('admin_dash')


def blacklisted(request):

    if request.method == 'POST':
        company_id = request.POST['company_id']
        company = Company.objects.get(id=company_id)
        company.approval_status = 'Blacklisted'
        company.save()
        return redirect('admin_dash')
    
    else:
        return redirect('admin_dash')