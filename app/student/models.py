from django.conf import settings
from django.db import models
from company.models import Drive

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    graduation_year = models.IntegerField(blank=True, null=True)
    resume = models.FileField(blank=True, null=True)
    blacklisted = models.BooleanField(default=False)


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE, null=False)
    application_date = models.DateField(blank=True, null=False)
    application_status = models.CharField(max_length=100, default='Applied', blank=True, null=False)