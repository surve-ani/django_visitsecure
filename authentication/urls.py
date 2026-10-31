from django.urls import path
from . import views

urlpatterns = [
    path('api/login/', views.LoginApiView.as_view(), name='api-login'),
]