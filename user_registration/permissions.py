# permissions.py
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an owner or an admin
        return request.user and (request.user.is_superuser or request.user.user_type == 'owner')

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        return request.user.user_type == 'admin'
    
class IsAdminUserOrIsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        return request.user.user_type == 'owner' or request.user.user_type == 'admin'
