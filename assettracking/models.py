from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
   
    def __str__(self):
        return f"{self.company_name} - {self.address}"
    

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10,unique=True)
    employee_dept = models.CharField(max_length=100,null=True)
    employee_contact = models.CharField(max_length=15,null=True)
    employee_gender = models.CharField(max_length=50,null=True)

    def __str__(self):
          return f"ID: {self.employee_id}, Name: {self.employee_name}, Dept: {self.employee_dept}, Contact: {self.employee_contact}, Gender: {self.employee_gender}"
    
class Device(models.Model):
    device_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    device_info = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[('assigned', 'Assigned'), ('available', 'Available')],
        default='available'
    )
    def __str__(self):
         return f"Serial Number: {self.serial_number}, Name: {self.device_name}, Info: {self.device_info}, Status: {self.status}"
    
class Allocation(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    serial_number = models.ForeignKey(Device, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    checkout_condition = models.TextField()
    return_condition = models.TextField()
    checkout_datetime = models.DateTimeField(auto_now_add=True)
    return_datetime = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('checked_out', 'Checked Out'), ('available', 'Available')],
        default='available'
    )

    def __str__(self):
        return f"{self.serial_number} assigned to {self. employee_id} from {self.start_date} to {self.end_date}"
