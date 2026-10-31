####
django-admin startproject

###

python3 manage.py startapp accounts
python3 manage.py startapp visitors
python3 manage.py startapp security
python3 manage.py startapp companies

### create the database tables
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py showmigrations

### Identify issue

python3 manage.py check

### Start Django server
python3 manage.py runserver

### Check installed packages
pip3 list | grep -i django   
pip3 list | grep -i drf

### If you want Swagger UI
pip3 install drf-yasg

Add to settings.py:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_yasg',
]

#Add to urls.py:

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="VisitSecure API",
      default_version='v1',
      description="API documentation for VisitSecure",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

### Flow


                    Django
                      │
             ┌────────┴────────┐
             │                 │
       Browser Login       API Login
          /login/         /api/login/
             │                 │
       Django Session          JWT
                               │
                               ↓
                         Swagger 🔒
                               │
                               ↓
                        request.user
                               │
                    ┌──────────┴──────────┐
                    │                     │
                  role                  user
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
        admin     manager   employee
          │         │         │
       IsAdmin  IsManager  IsEmployee


visitsecure/
│
├── config/
│
├── accounts/
│   ├── User
│   ├── Employee
│   └── Department
│
├── companies/
│   ├── Company    
│   ├── Branch
│   └── Gate
│
├── visitors/
│   ├── Visitor
│   └── Visit
│
├── security/
│   └── SecurityEntry
│
└── manage.py


curl -X POST http://127.0.0.1:8001/api/companies/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg4MTczMjU5LCJpYXQiOjE3ODgxNzI5NTksImp0aSI6ImRhMTdkM2I4YmU3MTQ2M2JhNTkyMzMzNGZmN2U1NTIwIiwidXNlcl9pZCI6MX0.yd7amwtrD0RuiilvGZUJI4VRIcf5odc3DRSHzDgMu4A" \
-d '{
    "name": "Test Companyi",
    "address": "Pune",
    "phone_number": "9876543210",
    "email": "test@gmail.com",
    "website": "https://test.com"
}'

<Company

ABC Technologies
Pune

<branch

Company
   |
   +-- Pune Branch
   |
   +-- Mumbai Branch
   |
   +-- Bangalore Branch

<Department

Pune Branch
    |
    +-- HR
    +-- IT
    +-- Finance
    +-- Sales
    +-- Admin

Company
 └── Branch
      └── Department
           ├── IT
           ├── HR
           ├── Finance
           ├── Sales
           ├── Admin
           └── Security
                ├── Security Guard
                ├── Security Supervisor
                └── Security Officer

Step 10: Run migrations

Now execute:

python3 manage.py makemigrations


User
 ↓
Who are you?
What role do you have?

Employee
 ↓
Where do you work?
Which company?
Which branch?
Which department?
What position?

