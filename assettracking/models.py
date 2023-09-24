from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

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
    device_info = models.TextField()
    status = models.CharField(max_length=20, default='available')

    def __str__(self):
        return f"{self.device_name} ({self.serial_number})"

class Allocation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
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
    def clean(self):
        # Validate that start_date is before end_date
        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date.")

    def __str__(self):
        return f"{self.device.serial_number} assigned to {self.employee.employee_name} from {self.start_date} to {self.end_date}"    
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Device: {self.device}, Event Type: {self.event_type}"
