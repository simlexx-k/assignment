from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import logging

logger = logging.getLogger(__name__)

class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifier
    for authentication instead of usernames. The manager
    supports creating users and superusers.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        try:
            user.set_password(password)
            user.save(using=self._db)
            logger.info(f"User created successfully with email: {email}")
        except Exception as e:
            logger.error(f"Error creating user with email: {email}. Error: {e}", exc_info=True)
            raise e
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        try:
            return self.create_user(email, password=password, **extra_fields)
        except Exception as e:
            logger.error(f"Error creating superuser with email: {email}. Error: {e}", exc_info=True)
            raise e


class User(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure the email field is unique
    is_teacher = models.BooleanField(default=False)  # Added field to identify if the user is a teacher
    is_learner = models.BooleanField(default=False)  # Added field to identify if the user is a learner

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    resources = models.FileField(upload_to='resources/%Y/%m/%d/', null=True, blank=True)
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    learner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    submitted_file = models.FileField(upload_to='submissions/%Y/%m/%d/')
    submission_time = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)  # Allow null for submissions not yet graded
    feedback = models.TextField(null=True, blank=True)  # Allow null for submissions not yet graded

    class Meta:
        unique_together = ('assignment', 'learner')

    def __str__(self):
        return f'Submission for {self.assignment.title} by {self.learner.email}'