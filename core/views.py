from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages

def send_email(to, subject, content, sender, file):
    mail = EmailMessage(subject, content, sender, [to])
    if file is not None:
        for f in file:
            mail.attach(f.name, f.read(), f.content_type)
    mail.send(fail_silently=True)

def index(request):
    if request.POST:
        sent_to = request.POST.get('to')
        sub = request.POST.get('sub')
        msg = request.POST.get('to')
        file = request.FILES.getlist('file')
        # file = request.FILES.get('file')
        print(file)
        
        print('got them successfully')
        # SendMail.objects.create(to=sent_to, subject=sub, content=msg)
        send_email(sent_to, sub, msg, settings.EMAIL_HOST_USER, file)
        messages.success(request, 'Email Sent Successfully')
        return redirect('index')
    return render(request, 'index.html')