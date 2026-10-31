from django.shortcuts import render

# Create your views here.

def security_dashboard(request):
    return render(request, 'security/dashboard.html')