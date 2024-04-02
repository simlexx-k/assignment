from django.contrib import admin
from .models import User, Assignment, Submission
import logging

logger = logging.getLogger(__name__)

# Register your models here.
try:
    admin.site.register(User)
    logger.info("User model registered successfully with the admin site.")
except Exception as e:
    logger.error(f"Error registering User model with the admin site: {e}", exc_info=True)

try:
    admin.site.register(Assignment)
    logger.info("Assignment model registered successfully with the admin site.")
except Exception as e:
    logger.error(f"Error registering Assignment model with the admin site: {e}", exc_info=True)

try:
    admin.site.register(Submission)
    logger.info("Submission model registered successfully with the admin site.")
except Exception as e:
    logger.error(f"Error registering Submission model with the admin site: {e}", exc_info=True)