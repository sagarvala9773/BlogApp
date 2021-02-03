from django import forms
from django.forms.widgets import PasswordInput

class UserData(forms.Form):
    name=forms.CharField(max_length=30,initial='nayan',help_text='This is name of user')
    email=forms.EmailField()
    password=forms.CharField(widget=PasswordInput)
