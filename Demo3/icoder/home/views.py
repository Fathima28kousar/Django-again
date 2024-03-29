from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import *
from django.core.exceptions import ValidationError
from blog.models import *
from django.http import HttpResponseNotAllowed
from django.contrib.auth import authenticate,login,logout


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
    query = request.GET.get('query')
    if query:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsAuthor, allPostsContent)
        
        if allPosts.count() == 0:
            messages.warning(request, 'No search results found. Please refine your query.')
    else:
        allPosts = Post.objects.none()
        messages.warning(request, 'No search query provided.')
        
    return render(request, 'home/search.html', {'allPosts': allPosts, 'query': query})

def about(request):
    return render(request,'home/about.html')


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(username) < 10:
            messages.error(request,"Your username must be in 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,'username should only contain letters and numbers')
            return redirect('home')
        if (pass1 != pass2):
            messages.error(request,'passwords do not match')
            return redirect('home')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('home')
        #Create the user
        myuser = User.objects.create_user(username,email,pass1) #this is used for password hashing also
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Registered Succesfully')
        return redirect('home')
    
    else:
        return HttpResponse('404 not found')

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials ! Please Try again')
            return redirect('home')
    return HttpResponse('404 Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect('home')