from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Contributor, Task
from .serializers import ContributorSerializer, TaskSerializer
from .forms import ContributorForm


def add_contributor(request):
    """View to add a new contributor."""
    if request.method == 'POST':
        form = ContributorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_contributor')
    else:
        form = ContributorForm()
    
    contributors = Contributor.objects.all()
    return render(request, 'tms/add_contributor.html', {'form': form, 'contributors': contributors})


class ContributorViewSet(viewsets.ModelViewSet):
    """ViewSet for Contributor model."""
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for Task model."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer