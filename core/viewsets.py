from rest_framework import viewsets
from .models import Assignment
from .serializers import AssignmentSerializer
import logging

logger = logging.getLogger(__name__)

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
            logger.info("Assignment created successfully.")
        except Exception as e:
            logger.error("Failed to create assignment.", exc_info=True)
            raise e

    def perform_update(self, serializer):
        try:
            serializer.save()
            logger.info("Assignment updated successfully.")
        except Exception as e:
            logger.error("Failed to update assignment.", exc_info=True)
            raise e

    def perform_destroy(self, instance):
        try:
            instance.delete()
            logger.info("Assignment deleted successfully.")
        except Exception as e:
            logger.error("Failed to delete assignment.", exc_info=True)
            raise e