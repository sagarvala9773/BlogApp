from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
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


def log_out(request):
    if request.user.is_authenticated:
        print(request.user.username)
        logout(request)
        messages.add_message(request,messages.SUCCESS,'Thankyou For visiting out site')
        return render(request,'logout.html')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'forms':fm})

def userprofile(request):
    if request.user.is_authenticated:
        messages.add_message(request,messages.SUCCESS,'Welcome to out site')
        u=request.user
        
        return render(request,'profile.html',{'user':u})

    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'forms':fm})


def change_password(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'changepassword.html',{'forms':fm})
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'forms':fm})


