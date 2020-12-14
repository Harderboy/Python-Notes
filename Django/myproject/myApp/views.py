from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("sunk is good man!")


def vote(request, num):
    return HttpResponse("detail-%s" % (num))


def detail(request, num1, num2):
    return HttpResponse("detail-%s-%s" % (num1, num2))


from .models import Grades, Students


def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回浏览器
    return render(request, 'myApp/grades.html', {'grades': gradesList})


def students(request):
    studentsList = Students.objects.all()
    return render(request, 'myApp/students.html', {'students': studentsList})


def gradesStudents(request, num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {'students': studentsList})
