from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profiles

# Create your views here.
def Register(request):
    return render(request, 'authentication/register.html')

def Signing_Up(request):
    New_User = User.objects.create(
        username = request.POST.get('UserName_Input'),
        password = request.POST.get('Password_Input'),
        email    = request.POST.get('Email_Input'),
    )
    New_User.first_name = request.POST.get('FirstName_Input')
    New_User.last_name = request.POST.get('LastName_Input')
    New_User.set_password(request.POST.get('Password_Input'))
    New_User.save()
    user_instance = User.objects.get(username=request.POST.get('UserName_Input'))
    ID = "QP%s" %str(user_instance.id).zfill(10)
    New_Profile = Profiles.objects.create(
        UserName  = user_instance,
        ID_User   = ID,
        FirstName = request.POST.get('FirstName_Input'),
        LastName  = request.POST.get('LastName_Input')
    )
    New_Profile.save()
    return render(request, 'authentication/login.html')


def Login(request):
    if request.user.is_authenticated:
        return HttpResponse('Logged In')
    else:
        return render(request, 'authentication/login.html')


def Logging(request):
    Username = request.POST.get('UserName_Input')
    Password = request.POST.get('Password_Input')
    print(Username, "-----------", Password)
    user_auth = authenticate(username=Username, password=Password)
    if user_auth is not None:
        login(request, user_auth)
        return HttpResponse('Login Done')
    else:
        print('User   :', user_auth)
        return render(request, 'authentication/login.html')
