from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}

class UserProfile(UserChangeForm):

    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined','is_active']
        labels={'email':'Email'}

class AdminProfile(UserChangeForm):

    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}