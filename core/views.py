from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import urllib.parse
from contact.forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            subject = f"New Enquiry from {contact_msg.name}"
            message = f"Name: {contact_msg.name}\nPhone: {contact_msg.phone}\nEmail: {contact_msg.email}\nService: {contact_msg.service_required}\nMessage: {contact_msg.message}"
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=True)
            except Exception:
                pass
            
            # Generate WhatsApp Redirect URL
            wa_text = f"Hello, I have a new enquiry.\n\n*Name:* {contact_msg.name}\n*Phone:* {contact_msg.phone}\n*Email:* {contact_msg.email}\n*Service:* {contact_msg.service_required}\n*Message:* {contact_msg.message}"
            wa_url = f"https://wa.me/918124428358?text={urllib.parse.quote(wa_text)}"
            
            messages.success(request, 'Your enquiry has been submitted. Redirecting to WhatsApp...')
            return redirect(wa_url)
        else:
            messages.error(request, 'There was an error submitting your form. Please check the details and try again.')
            return redirect('/#contact')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'gallery.html')

def process(request):
    return render(request, 'process.html')

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            subject = f"New Enquiry from {contact_msg.name}"
            message = f"Name: {contact_msg.name}\nPhone: {contact_msg.phone}\nEmail: {contact_msg.email}\nService: {contact_msg.service_required}\nMessage: {contact_msg.message}"
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=True)
            except Exception:
                pass
            
            # Generate WhatsApp Redirect URL
            wa_text = f"Hello, I have a new enquiry.\n\n*Name:* {contact_msg.name}\n*Phone:* {contact_msg.phone}\n*Email:* {contact_msg.email}\n*Service:* {contact_msg.service_required}\n*Message:* {contact_msg.message}"
            wa_url = f"https://wa.me/918124428358?text={urllib.parse.quote(wa_text)}"
            
            messages.success(request, 'Your enquiry has been submitted. Redirecting to WhatsApp...')
            return redirect(wa_url)
        else:
            messages.error(request, 'There was an error submitting your form. Please check the details and try again.')
        return redirect('contact')
    return render(request, 'contact.html')
