from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not user.is_active:
                return render(request, 'accounts/login.html', {'error': 'Your account is inactive. Please contact the administrator.'})
            login(request, user)
            print("---login_view---")  # Debugging statement
            print(f"User role: {user.role}")  # Debugging statement
            if user.role == 'admin':
                return redirect('/admin/') # Redirect to admin dashboard 
            elif user.role == 'employee':
                return redirect('employee_dashboard')  # Redirect to employee dashboard
            elif user.role == 'manager':
                return redirect('manager_dashboard')  # Redirect to manager dashboard
            elif user.role == 'supervisor':
                return redirect('supervisor_dashboard')  # Redirect to supervisor dashboard
            elif user.role == 'security':
                print("Redirecting to security dashboard")
                return redirect('security_dashboard') # Redirect to security dashboard
            elif user.role == 'hr':
                return redirect('hr_dashboard')  # Redirect to HR dashboard
            else:
                return redirect('dashboard')  # Redirect to a default dashboard if role is not recognized
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    return render(request, 'accounts/register.html')

def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

def profile_view(request):
    return render(request, 'accounts/profile.html')