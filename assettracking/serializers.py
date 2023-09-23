from rest_framework import serializers
from .models import Company, Employee, Device, Allocation

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = '__all__'





