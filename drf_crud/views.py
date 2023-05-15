import pprint

from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser

from .models import *
from .serializers import *


# Create your views here.
def index(request):
    return render(request, 'drf_crud/index.html', {'var': 'var'})


@csrf_exempt
def department(request, id=0):
    if request.method == "GET":

        data = Departments.objects.all()
        data_serialaizer = DepartmentSerializer(data, many=True)
        return JsonResponse(data_serialaizer.data, safe=False)
    elif request.method == "POST":

        data = JSONParser().parse(request)
        data_serializer = DepartmentSerializer(data=data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse('Create Good', safe=False)
        return JsonResponse('Failed', safe=False)
    elif request.method == 'DELETE':
        data = Departments.objects.get(DepartmentId=id)
        data.delete()
        return JsonResponse('Delete Good', safe=False)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        data_get = Departments.objects.get(DepartmentId=data['DepartmentId'])
        data_serializer = DepartmentSerializer(data_get, data=data)
        if data_serializer.is_valid():
            data_serializer.save()
            return JsonResponse('Update Good', safe=False)
        return JsonResponse('Failed', safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


class CarAPIList(generics.ListCreateAPIView):
    """ Отображение списка на странице"""
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
