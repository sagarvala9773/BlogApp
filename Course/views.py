from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def home(request):
    f1={'name':'sagar','age':19,'roll_no':146}
    return render(request, 'index.html',{'form':f1})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')  