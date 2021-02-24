from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Lab09.forms import StudentForm
from Lab09.models import Student

# Create your views here.
def home(request):
    if(request.method=='POST'):
        s1=StudentForm(request.POST)
        if s1.is_valid():
            name=s1.cleaned_data['name']
            roll_no=s1.cleaned_data['roll_no']
            email=s1.cleaned_data['email']
            password=s1.cleaned_data['password']
            stu=Student(name=name,roll_no=roll_no,email=email,password=password)
            stu.save()
        fm=StudentForm()
        obj=Student.objects.all()
    else:
        fm=StudentForm()
        obj=Student.objects.all()
    return render(request,'Home.html',{'form':fm,'obj':obj})



def update_data(request,id):
    if request.method=="POST":
        pi=Student.objects.get(roll_no=id)
        s1=StudentForm(request.POST,instance=pi)
        if s1.is_valid():
            pi.save()
        fm=StudentForm(instance=pi)
    else:
        pi=Student.objects.get(roll_no=id)
        fm=StudentForm(instance=pi)
    return render(request,'update.html',{'form':fm})


def delete_data(request,id):
    if request.method=="POST":
        pi=Student.objects.get(roll_no=id)
        pi.delete()
    return HttpResponseRedirect('/')

