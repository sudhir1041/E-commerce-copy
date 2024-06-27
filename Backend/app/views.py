from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is working")
