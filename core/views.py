from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("index view")

def appointment(request):
    return HttpResponse("appointment view")

def success(request):
    return HttpResponse("succ view")