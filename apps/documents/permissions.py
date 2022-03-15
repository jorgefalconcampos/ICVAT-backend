from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    message = "Not an owner"
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        print(obj)    
        return request.user == obj.author