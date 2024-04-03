from django.contrib import admin
from .models import User, Assignment, Submission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_teacher', 'is_learner', 'admission_number', 'is_staff', 'is_active')
    list_filter = ('is_teacher', 'is_learner', 'is_staff', 'is_active')
    search_fields = ('email', 'admission_number')
    ordering = ('email',)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline', 'created_at', 'updated_at')
    list_filter = ('deadline',)
    search_fields = ('title', 'description')
    ordering = ('-deadline',)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'learner', 'submission_time', 'grade')
    list_filter = ('assignment', 'learner', 'submission_time')
    search_fields = ('assignment__title', 'learner__email', 'grade')
    ordering = ('-submission_time',)