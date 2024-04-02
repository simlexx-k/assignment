from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CustomAuthForm, LearnerRegistrationForm
from django.contrib import messages
from .models import User
import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Assignment, Submission
from .serializers import AssignmentSerializer, SubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacherOrReadOnly
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)  # Changed from email=email to username=email
            if user is not None:
                login(request, user)
                logger.info(f"User {email} logged in successfully.")
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                messages.error(request, "Invalid login details")
                logger.warning(f"Failed login attempt for email: {email}. Invalid login details.")
        else:
            messages.error(request, "Invalid form submission")
            logger.error("Login form submission is invalid.")
    else:
        form = CustomAuthForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def dashboard(request):
    try:
        if request.user.is_teacher:
            assignments = Assignment.objects.all()
            submissions = Submission.objects.filter(grade__isnull=True)
            context = {'assignments': assignments, 'submissions': submissions}
            logger.info("Teacher dashboard loaded successfully.")
        elif request.user.is_superuser:
            users_count = User.objects.count()
            assignments_count = Assignment.objects.count()
            submissions_count = Submission.objects.count()
            context = {'users_count': users_count, 'assignments_count': assignments_count, 'submissions_count': submissions_count}
            logger.info("Admin dashboard loaded successfully.")
        else:
            learner_submissions = Submission.objects.filter(learner=request.user)
            context = {'learner_submissions': learner_submissions}
            logger.info("Learner dashboard loaded successfully.")
        return render(request, 'core/dashboard.html', context)
    except Exception as e:
        logger.error("Error loading dashboard.", exc_info=True)
        messages.error(request, "An error occurred while trying to load the dashboard.")
        return redirect('login')

def logout_view(request):
    try:
        logout(request)
        logger.info("User logged out successfully.")
        return redirect('login')
    except Exception as e:
        logger.error("Error during logout process.", exc_info=True)
        messages.error(request, "An error occurred while trying to log out.")
        return redirect('login')

def register_learner(request):
    if request.method == 'POST':
        form = LearnerRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = form.cleaned_data.get('admission_number')  # Use admission number as username
                user.set_unusable_password()  # As learners log in with admission numbers
                user.is_learner = True
                user.save()
                logger.info(f"Learner {user.username} registered successfully.")
                return redirect('login')
            except Exception as e:
                logger.error("Failed to register learner.", exc_info=True)
                messages.error(request, "An error occurred during registration.")
        else:
            messages.error(request, "Invalid form submission")
            logger.error("Registration form submission is invalid.")
    else:
        form = LearnerRegistrationForm()
    return render(request, 'core/register.html', {'form': form})