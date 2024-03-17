from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.core.exceptions import ValidationError

def home(request):
     return render(request,'home/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content) <4:
            messages.error(request,'Please fill the form correctly')
        else:
            try:
                contact = Contact.objects.create(
                    name = name,
                    email = email,
                    phone = phone,
                    content = content
                )
                messages.success(request,'Your message has been successfully sent')
                return redirect('contact')
            except ValidationError:
                messages.error(request,"Error occured while saving your message")
    return render(request,'home/contact.html')

def search(request):
    return render(request,'home/search.html')

def about(request):
    return render(request,'home/about.html')


# def handleSignUp(request):
#     return render()

# def handleLogin(request):

# def handleLogout(request):