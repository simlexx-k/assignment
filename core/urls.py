from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login_view, dashboard, logout_view, register_learner, admin_dashboard, generate_assignment_report
from .viewsets import AssignmentViewSet
from .submission_viewset import SubmissionViewSet
from .api import LoginAPIView  # Import the LoginAPIView

router = DefaultRouter()
router.register(r'assignments', AssignmentViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(router.urls)),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register_learner, name='register'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('generate_report/<int:assignment_id>/', generate_assignment_report, name='generate_assignment_report'),
    path('api/login', LoginAPIView.as_view(), name='api_login'),  # Add the API login route without trailing slash
]