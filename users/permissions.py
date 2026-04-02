from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Allows access only to Admin users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')

class IsAnalyst(permissions.BasePermission):
    """
    Allows access to Admin and Analyst users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role in ['admin', 'analyst'])

class IsViewer(permissions.BasePermission):
    """
    Allows access to all authenticated users (Viewer, Analyst, Admin).
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

class ReadOnlyPermission(permissions.BasePermission):
    """
    Allows read-only access to Viewer, and full access to Admin/Analyst.
    But for records, Viewer is read-only.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return request.user and request.user.role in ['admin', 'analyst']
