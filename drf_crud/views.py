from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializers import *


# Create your views here.
def index(request):
    return render(request, 'drf_crud/index.html', {'var': 'var'})


def req(request):
    data = Departments.objects.all()
    data_seris = DepartmentSerializer(data, many=True)
    return JsonResponse(data_seris.data, safe=False)


class CarAPIList(generics.ListCreateAPIView):
    """ Отображение списка на странице"""
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer