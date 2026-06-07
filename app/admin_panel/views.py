from django.shortcuts import render, redirect
from company.models import Company, Drive
from student.models import Student, Application
from django.contrib.auth.decorators import login_required

@login_required


def admin_dash(request):

    pending_companies = Company.objects.filter(approval_status='Pending')
    approved_companies = Company.objects.filter(approval_status='Approved')
    blacklisted_companies = Company.objects.filter(approval_status='Blacklisted')
    approved_students = Student.objects.filter(blacklisted=False)
    ongoing_drives = Drive.objects.filter(completed=False)
    applications = Application.objects.filter()
    is_admin = True

    context = {
        'pending_companies': pending_companies, 
        'approved_companies': approved_companies,
        'blacklisted_companies': blacklisted_companies,
        'approved_students': approved_students,
        'ongoing_drives': ongoing_drives,
        'applications': applications,
        'is_admin': is_admin,
        }
    
    return render(request, 'admin_panel/admin_dash.html', context)


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
    

def complete_drive(request):

    if request.method == "POST":
        drive_id = request.POST['drive_id']
        drive = Drive.objects.get(id=drive_id)
        drive.completed = True
        drive.save()
        return redirect('admin_dash')
    
    else:
        return redirect('admin_dash')
    

def student_application(request, application_id):
    application = Application.objects.get(id=application_id)
    student = application.student
    drive = application.drive
    
    context = {
        'application': application,
        'student': student,
        'drive': drive,
    }
    return render(request, 'company/student_application.html', context)


def drive_details(request, company_id, drive_id):
    company = Company.objects.get(id=company_id)
    drive = Drive.objects.get(id=drive_id)

    context ={
        'drive': drive, 
        'company': company,
    }
        
    return render(request, 'student/drive_details.html', context)
