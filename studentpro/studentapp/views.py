from django.shortcuts import render
from .models import Student

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        course = request.POST.get('course')

        Student.objects.create(name=name, roll=roll, course=course)

        return render(request, 'add.html', {'msg': 'Saved Successfully ✅'})

    return render(request, 'add.html')


def display_student(request):
    students = Student.objects.all()
    return render(request, 'display.html', {'students': students})