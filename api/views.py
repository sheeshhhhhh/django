from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import User
import bcrypt

# Create your views here.
@csrf_exempt
def Login(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.get(username=username)

        if(not(user)):
            return JsonResponse({ 
                "status" : "fail", 
                "message" : "wrong username", 
                "inputError" : "username" }, status=400)

        isPasswordValid = bcrypt.checkpw(password, user.password)

        if(not(isPasswordValid)):
            return JsonResponse({
                "status" : "fail",
                "message": "wrong password",
                "inputError": "password"
        }, status=400)

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return JsonResponse({ "status" : "success", "message" : "Successfully login" }, status=200)