from django.db import models

# Create your models here.
class Company(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    
    id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='branches')
    address = models.TextField()

    def __str__(self):
        return f"{self.branch_name} - {self.company.name}"

class Department(models.Model):
    department_name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='departments')
    
    def __str__(self):
        return f"{self.department_name} - {self.branch.branch_name}"
