# asset_tracking/views.py
from rest_framework import generics,status
from django.utils import timezone
from rest_framework.response import Response
from .models import Company, Employee, Device, Allocation
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, AllocationSerializer

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class AllocationListCreateView(generics.ListCreateAPIView):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer

class AllocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer




class DeviceAssignView(generics.CreateAPIView):
    queryset = Device.objects.filter(status='available')  # Only available devices can be assigned
    serializer_class = AllocationSerializer

    def perform_create(self, serializer):
        # Get the assigned employee from the serializer
        assigned_employee = serializer.validated_data['employee']
        
        # Check if the device is already assigned to another employee
        existing_allocation = Allocation.objects.filter(
            device=self.queryset.first(),  # Get the first available device
            status='checked_out'  # Check if it's already checked out
        ).first()
        
        if existing_allocation:
            return Response({'detail': 'Device is already assigned to another employee.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If not already assigned, create the allocation record and update the device status
        serializer.save()
        device = self.queryset.first()
        device.status = 'assigned'
        device.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DeviceReturnView(generics.UpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = AllocationSerializer

    def update(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            # Check if the device is already available (not assigned)
            if instance.status == 'available':
                return Response({'detail': 'Device is already available for assignment.'}, status=status.HTTP_400_BAD_REQUEST)

            # If the device is being returned, update the allocation record and device status
            serializer.save(status='checked_in', return_datetime=timezone.now())
            instance.status = 'available'
            instance.save()

            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

