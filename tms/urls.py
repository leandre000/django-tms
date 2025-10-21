from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContributorViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'contributors', ContributorViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [path('', include(router.urls))]
