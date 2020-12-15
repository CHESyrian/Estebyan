from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/authentication/login/')
def Search(request):
    keywords =  request.POST.get('SearchInput')
    if " " in keywords:
        keywords = keywords.split(' ')
        keywords = list(filter(lambda x : x != '', keywords))
        print(keywords)
    return HttpResponse(keywords)
