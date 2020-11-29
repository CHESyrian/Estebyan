from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from Questionnaire.models import Questionnaires
from Accounts.models import Profiles

# Create your views here.
def Register(request):
    Context = {
        "MsgError" : ""
    }
    return render(request, 'authentication/register.html', Context)

def Signing_Up(request):
    New_User = User.objects.create_user(
        username = request.POST.get('Reg_UserName_Input'),
        password = request.POST.get('Reg_Password_Input'),
        email    = request.POST.get('Email_Input'),
    )
    New_User.first_name = request.POST.get('FirstName_Input')
    New_User.last_name = request.POST.get('LastName_Input')
    #if you use User.objects.create you must user set_password() method.
    #New_User.set_password(request.POST.get('Password_Input'))
    New_User.save()
    user_instance = User.objects.get(username=request.POST.get('Reg_UserName_Input'))
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
    Username = request.POST.get('Log_UserName_Input')
    Password = request.POST.get('Log_Password_Input')
    user_auth = authenticate(username=Username, password=Password)
    if user_auth is not None:
        login(request, user_auth)
        return HttpResponseRedirect(reverse('MyProfile', args=[request.user.username]))
    else:
        print('User   :', user_auth)
        return render(request, 'authentication/login.html')


def Username_Validate(request, usrnm):
    special_chars  = "<{[(,`'\"\\-;:~!+=?@#$%^&*/)]}>"
    check_username = User.objects.filter(username=usrnm).exists()
    username       = usrnm
    if not check_username:
        return JsonResponse({"status":True, "error":""})
    else:
        return JsonResponse({"status":False,"error":"Username is already exist.Please, try another name"})
