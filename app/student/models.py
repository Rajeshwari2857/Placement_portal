from django.conf import settings
from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    department = models.CharField(blank=True, null=True)
    drive = models.IntegerField(blank=True, null=True)
    resume = models.FileField(blank=True, null=True)
