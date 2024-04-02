# ./core/serializers.py

from rest_framework import serializers
from .models import Assignment, Submission
import logging

logger = logging.getLogger(__name__)

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    grade = serializers.FloatField(required=False)
    feedback = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'learner', 'submitted_file', 'submission_time', 'grade', 'feedback']
        read_only_fields = ['learner', 'submission_time']

    def update(self, instance, validated_data):
        try:
            instance.grade = validated_data.get('grade', instance.grade)
            instance.feedback = validated_data.get('feedback', instance.feedback)
            instance.save()
            logger.info(f"Submission {instance.id} updated successfully with grade and feedback.")
            return instance
        except Exception as e:
            logger.error(f"Failed to update submission {instance.id} with grade and feedback. Error: {e}", exc_info=True)
            raise e