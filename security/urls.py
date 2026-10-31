from django.urls import path
from . import views

urlpatterns = [
    path('security/dashboard/', views.security_dashboard, name='security_dashboard'),
]