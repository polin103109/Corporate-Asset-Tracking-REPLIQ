#rom django.shortcuts import render

from rest_framework import generics
from .models import Company, Employee, Device, Allocation
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, AllocationSerializer

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class AllocationListCreateView(generics.ListCreateAPIView):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer

