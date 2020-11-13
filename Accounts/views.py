from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Authentication.models import Profiles


@login_required(login_url='/authentication/login/')
def MyProfile(request, usrnm):
    if usrnm == request.user.username:
        user_id = User.objects.get(username=usrnm).id
        Profile = Profiles.objects.get(UserName=user_id)
        Context = {
            'Profile' : Profile
        }
        return render(request, 'Accounts/my_profile.html', Context)
    else:
        return HttpResponse('Permission Denied')
