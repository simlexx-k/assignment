from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)

class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            logger.warning("Unauthorized access attempt.")
            return False
        is_teacher = request.user.is_teacher
        if is_teacher:
            logger.info("Access granted to teacher.")
        else:
            logger.warning("Access denied. User is not a teacher.")
        return is_teacher