from django.contrib import admin
from app.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_value', 'second_value', 'result', 'created_at',)
    search_fields = ('name',)
    list_filter = ('name',)