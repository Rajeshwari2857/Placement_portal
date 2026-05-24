from django.conf import settings
from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    drive = models.IntegerField(blank=True, null=True)
    resume = models.FileField(blank=True, null=True)
    blacklisted = models.BooleanField(default=False)