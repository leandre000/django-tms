from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


class Contributor(models.Model):
    """Model representing a contributor in the task management system."""
    
    ROLE_CHOICES = [
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('manager', 'Manager'),
        ('tester', 'Tester'),
        ('analyst', 'Analyst'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('on_leave', 'On Leave'),
    ]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='contributor_profile',
        null=True,
        blank=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='developer')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='contributors/', blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'Contributor'
        verbose_name_plural = 'Contributors'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_active_tasks_count(self):
        """Return the count of active tasks assigned to this contributor."""
        return self.tasks.filter(status='in_progress').count()


class Task(models.Model):
    """Model representing a task in the system."""
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('review', 'In Review'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    assigned_to = models.ForeignKey(
        Contributor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_tasks'
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        return f"{self.title} - {self.status}"
    
    def is_overdue(self):
        """Check if the task is overdue."""
        from django.utils import timezone
        if self.due_date and self.status not in ['completed', 'cancelled']:
            return timezone.now().date() > self.due_date
        return False
