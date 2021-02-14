from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import CreateUser
from django.contrib import messages
# Create your views here.

def log_in(request):

    if request.method == "POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')

    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'forms':fm})


def sign_up(request):
    if request.method == "POST":
        fm=CreateUser(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thanks for sign up')
            return HttpResponseRedirect('/conformation/')
        
    else:
        fm=CreateUser()
    return render(request,'signup.html',{'forms':fm})


def conform(request):
    return render(request,'conform.html')

def userprofile(request):
    return render(request,'profile.html')