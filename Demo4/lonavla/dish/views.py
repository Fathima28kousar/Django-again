from django.shortcuts import render

def dish(request):
    return render(request,'dish.html')

def update(request):
    return render(request,'update.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')