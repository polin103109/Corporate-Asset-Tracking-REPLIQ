# assettracking/views.py
from rest_framework import generics
from .models import Company,Employee,Device,Allocation,DeviceLog
from .serializers import CompanySerializer,EmployeeSerializer,DeviceSerializer,DeviceAllocationSerializer,DeviceLogSerializer

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
class DeviceAllocationListCreateView(generics.ListCreateAPIView):
    queryset = Allocation.objects.all()
    serializer_class = DeviceAllocationSerializer
class DeviceLogListCreateView(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
