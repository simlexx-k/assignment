from rest_framework import viewsets
from .models import Submission
from .serializers import SubmissionSerializer
import logging

logger = logging.getLogger(__name__)

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
            logger.info("Submission created successfully.")
        except Exception as e:
            logger.error("Failed to create submission. Error: %s", e, exc_info=True)
            raise e

    def perform_update(self, serializer):
        try:
            serializer.save()
            logger.info("Submission updated successfully.")
        except Exception as e:
            logger.error("Failed to update submission. Error: %s", e, exc_info=True)
            raise e

    def perform_destroy(self, instance):
        try:
            instance.delete()
            logger.info("Submission deleted successfully.")
        except Exception as e:
            logger.error("Failed to delete submission. Error: %s", e, exc_info=True)
            raise e