from django.contrib import admin

from .models import Task, Executor


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'comment', 'priority', 'created_at', 'executor']
    list_filter = ['title', 'priority']


@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]
