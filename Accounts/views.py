from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/authentication/login/')
def MyProfile(request, usrnm):
    if usrnm == request.user.username:
        Context = {
            'User' : usrnm
        }
        return render(request, 'Accounts/my_profile.html', Context)
    else:
        return HttpResponse('Permission Denied')
