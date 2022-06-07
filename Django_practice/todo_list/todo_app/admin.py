from django.contrib import admin
from .models import TodoListItem

# Register your models here.

@admin.register(TodoListItem)
class TodoListItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'content', 'complete', 'created']