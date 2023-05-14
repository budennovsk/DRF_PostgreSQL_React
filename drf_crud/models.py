from django.db import models


# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.DepartmentId}, {self.DepartmentName}"


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100, blank=True)
    Department = models.CharField(max_length=100, blank=True)
    DateOfJoining = models.DateField(auto_now=True)
    PhotoFileName = models.CharField(max_length=100, blank=True)
