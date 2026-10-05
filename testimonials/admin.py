from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'is_featured')
    list_filter = ('is_featured', 'rating')
    list_editable = ('is_featured',)
