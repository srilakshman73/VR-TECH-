from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            
            # Optional Email Notification
            subject = f"New Enquiry from {contact_msg.name}"
            message = f"Name: {contact_msg.name}\nPhone: {contact_msg.phone}\nEmail: {contact_msg.email}\nService: {contact_msg.service_required}\nMessage: {contact_msg.message}"
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            
            messages.success(request, 'Your enquiry has been submitted successfully! We will get back to you soon.')
        else:
            messages.error(request, 'There was an error submitting your form. Please check the details and try again.')
        return redirect('/#contact')
    return redirect('/')
