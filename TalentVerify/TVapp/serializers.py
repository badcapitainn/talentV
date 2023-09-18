from rest_framework import serializers
from TVapp.models import Company, Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'CompanyId',
            'CompanyName',
            'DateOfRegistration',
            'RegistrationNumber',
            'CompanyAddress',
            'ContactPerson',
            'ListofDepartments',
            'EmployeeNumber',
            'Phone',
            'Email',
        )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'EmployeeID',
            'EmployeeName',
            'Department',
            'EmployeeRole',
            'DateStarted',
            'DateLeft',
            'RoleDuties',
        )