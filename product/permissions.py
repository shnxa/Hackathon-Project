from rest_framework import permissions

class IsUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj.author

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return IsUserOrAdmin(),
        return permissions.AllowAny(),