from django.shortcuts import render
from .models import Course
def register_course(request):
    if request.method=="POST":
        name=request.POST.get('name')
        student=request.POST.get('student')
        email=request.POST.get('email')
        Course.objects.create(name=name,student=student,email=email)
        return render(request,'register.html',{'msg': 'Registered Suceesfully'})
    return render(request,'register.html')
def display_course(request):
    courses=Course.objects.all()
    return render(request,'display.html',{'courses':courses})

# Create your views here.
