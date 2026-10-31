from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Visitor(models.Model):

    class IDProofType(models.TextChoices):
        PASSPORT = 'Passport', 'Passport'
        DRIVERS_LICENSE = 'Driver\'s License', 'Driver\'s License'
        NATIONAL_ID = 'National ID', 'National ID'
        AADHAR_CARD = 'Aadhar Card', 'Aadhar Card   '
        OTHER = 'Other', 'Other'
    
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    id_proof_type = models.CharField(max_length=50, choices=IDProofType.choices, default=IDProofType.OTHER)
    id_proof_number = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"

class Visit(models.Model):

    class Purpose(models.TextChoices):
        INTERVIEW = 'Interview', 'Interview'
        MEETING = 'Meeting', 'Meeting'
        SERVICE = 'Service', 'Service'
        BUSINESS = 'Business', 'Business'
        PERSONAL = 'Personal', 'Personal'
        DELIVERY = 'Delivery', 'Delivery'
        OTHER = 'Other', 'Other'

    class Status(models.TextChoices):
        CHECKED_IN = 'Checked In', 'Checked In'
        CHECKED_OUT = 'Checked Out', 'Checked Out'

    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=20, choices=Purpose.choices, default=Purpose.OTHER)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(blank=True, null=True)
    check_in_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='check_in_by', blank=True, null=True)
    check_out_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='check_out_by', blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CHECKED_IN)

    def __str__(self):
        return f"Visit by {self.visitor.full_name} to {self.purpose} - Status: {self.status}"