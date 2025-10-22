from django.contrib import admin
from .models import Contributor, Task


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'is_present']
    search_fields = ['name', 'email']
    list_per_page = 20


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'contributor', 'start_date', 'due_date', 'is_completed']
    list_filter = ['is_completed', 'start_date', 'due_date']
    search_fields = ['title', 'contributor__name']
    list_editable = ['is_completed']
    list_per_page = 25
    date_hierarchy = 'start_date'