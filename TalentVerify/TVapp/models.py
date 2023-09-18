from django.db import models

class Company(models.Model):
    CompanyId = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=500)
    DateOfRegistration = models.DateField()
    RegistrationNumber = models.CharField(max_length=20)
    CompanyAddress = models.CharField(max_length=500)
    ContactPerson = models.CharField(max_length=100)
    ListofDepartments = models.CharField(max_length=700)
    EmployeeNumber = models.IntegerField()
    Phone = models.IntegerField()
    Email = models.EmailField()


class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=500)
    EmployeeRole = models.CharField(max_length=500)
    DateStarted = models.DateField()
    DateLeft = models.DateField()
    RoleDuties = models.CharField(max_length=500)