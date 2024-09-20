from rest_framework.permissions import BasePermission
from .models import *

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        student = Student.objects.get(user=request.user)
        if student:
            return True
        else:
            return False
        
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        ostad = Ostad.objects.get(user=request.user)
        if ostad:
            return True
        else:
            return False