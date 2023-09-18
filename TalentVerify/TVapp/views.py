from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from TVapp.models import Company, Employee
from TVapp.serializers import CompanySerializer, EmployeeSerializer

@csrf_exempt
def CompanyApi(request, id=0):
    if request.method == 'GET':
        company = Company.objects.all()
        company_serializer = CompanySerializer(company, many=True)
        return JsonResponse(company_serializer.data, safe=False)

    elif request.method == 'POST':
        company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data=company_data)

        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse('Successfully added', safe=False)
        return JsonResponse('Failed to add', safe=False)

    elif request.method == 'PUT':
        company_data = JSONParser().parse(request)
        company = Company.objects.get(CompanyId=company_data['CompanyId'])
        company_serializer = CompanySerializer(company, data=company_data)

        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse('Successfully Updated', safe=False)
        return JsonResponse('Failed to Update', safe=False)

    elif request.method == 'DELETE':
        company = Company.objects.get(CompanyId=id)
        company.delete()
        return JsonResponse('Successfully Deleted', safe=False)


@csrf_exempt
def EmployeeApi(request, id=0):
    if request.method == 'GET':
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)

        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Successfully added', safe=False)
        return JsonResponse('Failed to add', safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeID=employee_data['EmployeeID'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)

        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Successfully Updated', safe=False)
        return JsonResponse('Failed to Update', safe=False)

    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse('Successfully Deleted', safe=False)