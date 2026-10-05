from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_required', 'created_at', 'is_resolved')
    list_filter = ('is_resolved', 'service_required', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_editable = ('is_resolved',)
