from django import forms
from .models import Contributor, Task


class ContributorForm(forms.ModelForm):
    """Form for creating and editing Contributors with Tailwind CSS styling."""
    
    class Meta:
        model = Contributor
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 shadow-sm',
                'placeholder': 'Enter contributor name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 shadow-sm',
                'placeholder': 'Enter email address'
            }),
        }
        labels = {
            'name': 'Contributor Name',
            'email': 'Email Address',
        }


class TaskForm(forms.ModelForm):
    """Form for creating and editing Tasks with Tailwind CSS styling."""
    
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'contributor': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 shadow-sm'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 shadow-sm',
                'placeholder': 'Enter task title'
            }),
            'start_date': forms.DateTimeInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 shadow-sm',
                'type': 'datetime-local'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 shadow-sm',
                'type': 'datetime-local'
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-blue-600 border-gray-300 rounded focus:ring-2 focus:ring-blue-500 cursor-pointer'
            }),
        }
        labels = {
            'contributor': 'Assign to Contributor',
            'title': 'Task Title',
            'start_date': 'Start Date & Time',
            'due_date': 'Due Date & Time',
            'is_completed': 'Mark as Completed',
        }