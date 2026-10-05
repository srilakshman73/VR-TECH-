from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'order', 'uploaded_at')
    list_filter = ('project_type',)
    list_editable = ('order',)
