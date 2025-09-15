from django.contrib import admin
from .models import Task, Subtask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_complete', 'created_at')
    list_filter = ('is_complete', 'created_at')
    search_fields = ('title', 'description', 'owner__username')
    ordering = ('-created_at',)
    list_select_related = ('owner',)
    readonly_fields = ('created_at',)  
    
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'is_done', 'created_at')
    list_filter = ('is_done',)
    search_fields = ('title', 'task__title')
    ordering = ('-created_at',)
    list_select_related = ('task',)
    readonly_fields = ('created_at',)  