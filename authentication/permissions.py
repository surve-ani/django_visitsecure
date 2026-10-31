from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Custom permission to only allow admin users to access certain views.
    """

    def has_permission(self, request, view):
        print("===== RBAC CHECK =====")
        print("User:", request.user)
        print("Authenticated:", request.user.is_authenticated)
        print("Role:", getattr(request.user, 'role', None))
        return request.user and request.user.is_authenticated and request.user.role == 'admin'  

class IsSecurityUser(BasePermission):
    """
    Custom permission to only allow security users to access certain views.
    """

    def has_permission(self, request, view):
        print("===== RBAC CHECK =====")
        print("User:", request.user)
        print("Authenticated:", request.user.is_authenticated)
        print("Role:", getattr(request.user, 'role', None))
        return request.user and request.user.is_authenticated and request.user.role == 'security'