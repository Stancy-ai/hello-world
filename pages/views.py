from django.shortcuts import render
from django.http import HttpResponse

def homepageView(request):
    return HttpResponse('Hello, world')
