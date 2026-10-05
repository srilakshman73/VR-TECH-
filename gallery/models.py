from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    project_type = models.CharField(max_length=100, blank=True, help_text="E.g., Demo project, Concept demo")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-uploaded_at']

    def __str__(self):
        return self.title
