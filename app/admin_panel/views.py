from django.shortcuts import render
from company import models

# Create your views here.
def dashboard(request):
    companies = models.Company.objects.all()
    return render(request, 'admin_dash.html', {'companies': companies})
