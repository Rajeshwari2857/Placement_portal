from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    hr_contact = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    approval_status = models.CharField(max_length=200, default='pending')
