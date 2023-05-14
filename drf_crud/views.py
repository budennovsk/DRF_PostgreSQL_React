import pprint

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







class CarAPIList(generics.ListCreateAPIView):
    """ Отображение списка на странице"""
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
