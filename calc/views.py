from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'result.html')
def profile(reqest):
    return HttpResponse('i am profile')
def event(request):
    return render(request,'event.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
 