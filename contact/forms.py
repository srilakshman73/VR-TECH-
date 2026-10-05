from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'service_required', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'autocomplete': 'name'}),
            'phone': forms.TextInput(attrs={'required': True, 'autocomplete': 'tel', 'type': 'tel'}),
            'email': forms.EmailInput(attrs={'required': True, 'autocomplete': 'email'}),
            'service_required': forms.Select(),
            'message': forms.Textarea(),
        }
