from django.shortcuts import render, redirect
from company.models import Company
from student.models import Student


def admin_dash(request):

    pending_companies = Company.objects.filter(approval_status='Pending')
    approved_companies = Company.objects.filter(approval_status='Approved')
    blacklisted_companies = Company.objects.filter(approval_status='Blacklisted')
    approved_students = Student.objects.filter(blacklisted=False)

    companies = {
        'pending_companies': pending_companies, 
        'approved_companies': approved_companies,
        'blacklisted_companies': blacklisted_companies,
        'approved_students': approved_students,
        }
    
    return render(request, 'admin_dash.html', companies)


def approve_company(request):

    if request.method == 'POST':
        company_id = request.POST['company_id']
        company = Company.objects.get(id=company_id)
        company.approval_status = 'Approved'
        company.save()
        return redirect('admin_dash')
    
    else:
        return redirect('admin_dash')


def blacklist_company(request):

    if request.method == 'POST':
        company_id = request.POST['company_id']
        company = Company.objects.get(id=company_id)
        company.approval_status = 'Blacklisted'
        company.save()
        return redirect('admin_dash')
    
    else:
        return redirect('admin_dash')
    
def blacklist_student(request):

    if request.method == 'POST':
        student_id = request.POST['student_id']
        student = Student.objects.get(id=student_id)
        student.blacklisted = True
        student.save()
        return redirect('admin_dash')
    
    else:
        return redirect('admin_dash')
