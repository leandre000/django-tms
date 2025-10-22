from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContributorViewSet, TaskViewSet, add_contributor, mark_contributors

router = DefaultRouter()
router.register(r'contributors', ContributorViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contributors/add/', add_contributor, name='add_contributor'),
    path('contributors/list/', mark_contributors, name='mark_contributors'),
]
