from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm, UserChangeForm
from .forms import CreateUser,UserProfile,AdminProfile
from django.contrib import messages
from django.contrib.auth.models import User
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
        logout(request)
    return HttpResponseRedirect('/')

def userprofile(request):
    if request.user.is_authenticated:
        u=User.objects.all()
        if request.method=="POST":
            fm=UserProfile(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/')
        else:
            u=User.objects.all()
            fm=UserProfile(instance=request.user)
        return render(request,'profile.html',{'forms':fm,'users':u})

    return HttpResponseRedirect('/')


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

    return HttpResponseRedirect('/')

def show_user(request,my_id):
    if request.user.is_authenticated:
        fm=User.objects.get(pk=my_id)
   
        return render(request,'showuser.html',{'forms':fm})
    return HttpResponseRedirect('/')

def delete_user(request,my_id):
    if request.user.is_authenticated:
        fm=User.objects.get(pk=my_id)
        fm.delete()

    return HttpResponseRedirect('/')
