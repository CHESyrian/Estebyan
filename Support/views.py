from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/Authentication/login/')
def Contact(request):
    return HttpResponse('Contacted :)')


@login_required(login_url='/Authentication/login/')
def Report(request):
    return HttpResponse('Contacted :)')
