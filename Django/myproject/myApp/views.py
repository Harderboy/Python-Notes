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


from django.db.models import F, Q


def grades2(request):
    # 描述中带有“hua”的数据对应的班级
    gradesList = Grades.objects.filter(students__scontent__contains="hua")
    # gradesList = Grades.objects.filter(ggirlnum__lt=F('gboynum') - 50)
    return render(request, 'myApp/grades.html', {'grades': gradesList})


def students(request):
    # 返回包含所有 Students 对象的列表
    # studentsList = Students.objects.all()
    studentsList = Students.stuObject2.all()
    return render(request, 'myApp/students.html', {'students': studentsList})


def students2(request):
    # 返回包含所有 Students 对象的列表
    # studentsList = Students.objects.all()
    # 报异常，可以考虑添加try，或者换成filter()方法
    studentsList = Students.stuObject2.get(sgender=1)
    return render(request, 'myApp/students.html', {'students': studentsList})


# 显示前5条学生
def students3(request):
    studentsList = Students.stuObject2.all()[0:5]
    return render(request, 'myApp/students.html', {'students': studentsList})


# 分页显示学生
def stupage(request, page):
    # 0-5 5-10
    #  1   2
    page = int(page)
    studentsList = Students.stuObject2.all()[((page - 1) * 5):(page * 5)]
    return render(request, 'myApp/students.html', {'students': studentsList})


from django.db.models import Max


def studentsearch(request):
    # studentsList = Students.stuObject2.filter(pk__in=[2, 6, 7])
    # maxAge = Students.stuObject2.aggregate(Max("sage"))
    # print(maxAge)
    # studentsList = Students.stuObject2.filter(Q(pk__lte=3) | Q(sage__lt=23))
    studentsList = Students.stuObject2.filter(~Q(pk__lte=3))
    return render(request, 'myApp/students.html', {'students': studentsList})


def gradesStudents(request, num):
    # 获取指定班级的学生
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {'students': studentsList})


def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudents("刘德华", 34, True, "my name is hua", grade)
    stu.save()
    return HttpResponse("fadfa")


def addstudent2(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObject2.createStudents("李华", 32, True, "hello world",
                                             grade)
    stu.save()
    return HttpResponse("****")