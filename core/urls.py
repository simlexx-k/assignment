from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login_view, dashboard, logout_view
from .viewsets import AssignmentViewSet, SubmissionViewSet
router = DefaultRouter()
router.register(r'assignments', AssignmentViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(router.urls)),
    path('dashboard/', dashboard, name='dashboard'),
]