from django.contrib import admin

from .models import Company, Branch, Department
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')
    search_fields = ('name', 'address')
    ordering = ('name',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'company', 'address')
    search_fields = ('branch_name', 'company__name', 'address')
    ordering = ('branch_name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'branch')
    search_fields = ('department_name', 'branch__branch_name')
    ordering = ('department_name',)