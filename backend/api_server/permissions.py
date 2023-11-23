from rest_framework import permissions
from rest_framework.permissions import BasePermission
from api_service.models import CustomUser


# pylint: disable=no-member
class APIKeyPermission(BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get('X-API-KEY')

        if not api_key:
            return False

        try:
            user = CustomUser.objects.get(api_key=api_key)
            return user.api_key_status == 'active'
        except CustomUser.DoesNotExist:
            return False
        
        
class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS