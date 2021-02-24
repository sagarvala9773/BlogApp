from django import forms
from django.forms import fields, widgets
from Lab09.models import Student

class StudentForm(forms.ModelForm):
    password=forms.CharField(widget=widgets.PasswordInput)
    class Meta:
        model=Student
        fields=['name','roll_no','email','password']