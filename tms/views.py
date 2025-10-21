from rest_framework import viewsets
from .models import Contributor, Task
from .serializers import ContributorSerializer, TaskSerializer


class ContributorViewSet(viewsets.ModelViewSet):
    """ViewSet for Contributor model."""
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for Task model."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
