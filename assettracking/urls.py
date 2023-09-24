# asset_tracking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyDetailView.as_view(), name='company-detail'),
    
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),

    path('devices/', views.DeviceListCreateView.as_view(), name='device-list'),
    path('devices/<int:pk>/', views.DeviceDetailView.as_view(), name='device-detail'),

    path('allocations/', views.AllocationListCreateView.as_view(), name='allocation-list'),
    path('allocations/<int:pk>/', views.AllocationDetailView.as_view(), name='allocation-detail'),
   
    path('devices/assign/', views.DeviceAssignView.as_view(), name='device-assign'),
    path('devices/return/<int:pk>/', views.DeviceReturnView.as_view(), name='device-return'),
]
