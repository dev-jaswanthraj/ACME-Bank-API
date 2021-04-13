from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin of an object to edit it.
    """

    def has_permission(self, request, view):
        """Allow read permissions for any user"""
        if request.method in SAFE_METHODS:
            return True
        # Write permissions allowed only for admin
        return request.user.is_staff
