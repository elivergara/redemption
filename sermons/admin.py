from django.contrib import admin
from .models import Sermon

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
