from django.shortcuts import render

# Create your views here.

def SignUp(request):
    return render(request, 'my_auth/signup.html')

def Login(request):
    return render(request, 'my_auth/login.html')

