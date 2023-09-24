# asset_tracking/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from assettracking.views import (
    CompanyListCreateView,EmployeeListCreateView,DeviceListCreateView,DeviceAllocationListCreateView,DeviceLogListCreateView
)

router = DefaultRouter()

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('device-allocations/', DeviceAllocationListCreateView.as_view(), name='device-allocation-list-create'),
    path('device-logs/', DeviceLogListCreateView.as_view(), name='device-log-list-create'),
   
]

