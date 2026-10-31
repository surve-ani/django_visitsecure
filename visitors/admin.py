from django.contrib import admin

from .models import Visit, Visitor

# Register your models here.

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'company_name', 'id_proof_type', 'id_proof_number', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number', 'company_name', 'id_proof_type', 'id_proof_number')
    ordering = ('-created_at',)

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'purpose', 'check_in_time', 'check_out_time', 'check_in_by', 'check_out_by', 'status')
    search_fields = ('visitor__full_name', 'purpose', 'status')
    ordering = ('-check_in_time',)