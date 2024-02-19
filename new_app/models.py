from django.db import models


# Create your models here.
class EmployeeDetail(models.Model):
    designation = models.CharField(max_length=10)
    salary = models.FloatField()
