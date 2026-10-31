from django.urls import path
from . import views

urlpatterns = [
    path('api/companies/', views.CompanyListApiView.as_view(), name='company-list'),
    path('api/companies/<int:company_id>/', views.CompanyDetailApiView.as_view(), name='company-detail'),
    path('api/branches/', views.BranchListApiView.as_view(), name='branch-list'),
]