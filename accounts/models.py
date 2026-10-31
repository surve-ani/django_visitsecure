from django.db import models
from companies.models import Company, Branch, Department
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class User(AbstractUser):

    class Roles(models.TextChoices):
        EMPLOYEE = 'employee', 'Employee'
        MANAGER = 'manager', 'Manager'
        ADMIN = 'admin', 'Admin'
        SECURITY = 'security', 'Security'
        HR = 'hr', 'HR'

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.EMPLOYEE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Employee(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"