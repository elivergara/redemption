from django.contrib import admin

# Register your models here.

from .models import Event  # Import your Event model
from .models import AboutPage

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'pushpay_link')  # Include pushpay_link
    search_fields = ('title', 'description', 'pushpay_link')  # Searchable fields
    list_filter = ('created_at',)  # Filters in the admin sidebar


admin.site.register(AboutPage)
