from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Don't use this project")
