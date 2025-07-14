from rest_framework import permissions

class IsVendor(permissions.BasePermission):
    """
    Permission class to allow access only to user with 'vendor' role
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'vendor'
    
class IsUser(permissions.BasePermission):
    """
    Permission class to allow access only to user with 'user' role
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'

class IsSuperAdmin(permissions.BasePermission):
    """
    Permission class to allow access only to user with 'superaddmin' role
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'superadmin'