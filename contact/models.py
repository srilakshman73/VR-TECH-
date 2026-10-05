from django.db import models

class ContactMessage(models.Model):
    SERVICE_CHOICES = (
        ('Website Development', 'Website Development'),
        ('Mobile App Development', 'Mobile App Development'),
        ('Business Software Solutions', 'Business Software Solutions'),
        ('Cloud, Hosting & Domain', 'Cloud, Hosting & Domain'),
        ('Digital Marketing & SEO', 'Digital Marketing & SEO'),
        ('UI/UX & Branding', 'UI/UX & Branding'),
        ('AMC & Technical Support', 'AMC & Technical Support'),
        ('Other / Not sure yet', 'Other / Not sure yet'),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    service_required = models.CharField(max_length=100, choices=SERVICE_CHOICES, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"
