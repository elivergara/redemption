from django.contrib import admin

# Register your models here.

from .models import Event  # Import your Event model

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Columns to display in the admin list view
    search_fields = ('title', 'description')  # Searchable fields
    list_filter = ('created_at',)  # Filters in the admin sidebar
