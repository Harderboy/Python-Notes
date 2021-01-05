from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index1(request):  # request 浏览器请求
    # return HttpResponse("sunk is good man!")  # HttpResponse 浏览器响应
    return HttpResponseRedirect('/sunck')


def index(request):
    return render(request, 'myApp/index.html')


# 在浏览器地址输入栏中传参数num，只需在原有url后面添加新的内容，如'3/'或'3'
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
    # studentsList = Students.stuObject2.get(sgender=0)
    studentsList = Students.stuObject2.all()
    return render(request, 'myApp/students2.html', {'students': studentsList})


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


def attribute(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribute")


def get1(request):
    # a = request.GET.get['a']
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    # print(type(a))
    return HttpResponse(a + ' ' + b + ' ' + c)


def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + ' ' + a2 + ' ' + c)


# POST
def showregist(request):
    return render(request, 'myApp/regist.html')


def regist(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("post")


# response
def showresponse(request):
    res = HttpResponse()
    res.content = b'good'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content - type)
    return res


# cookie
def cookietest(request):
    res = HttpResponse()
    # cookie = res.set_cookie('sunck', 'good')
    cookie = request.COOKIES
    res.write("<h1>" + cookie['sunck'] + "</h1>")
    return res


# 重定向
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def redirect1(request):
    # return HttpResponseRedirect('/sunck/redirect2')
    return redirect('/sunck/redirect2')


def redirect2(request):
    return HttpResponse("<h1>我是重定向后的视图</h1>")


# session
def homepage(request):
    # 取session
    # username = "游客"
    username = request.session.get('name', "游客")
    return render(request, 'myApp/homepage.html', {'username': username})


def login(request):
    return render(request, 'myApp/login.html')


def showhomepage(request):
    username = request.POST.get('username')
    # 存储session
    request.session['name'] = username
    # request.session.set_expiry(10)
    return redirect('/sunck/homepage/')


from django.contrib.auth import logout


def quit(request):
    # 清除session,推荐使用logout(request)
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect('/sunck/homepage/')


# 模板语法
def getstudent(request):
    student = Students.stuObject2.get(pk=1)
    return render(
        request, 'myApp/index2.html', {
            'stu': student,
            'num': 10,
            'str': 'sunck is good man',
            'list': ['sunck', 'good', 'man'],
            'test': False,
            'code': '<h2>sunck is good!</h2>'
        })


# 反向解析
def good(request, num1, num2):
    return render(request, 'myApp/good.html', {'num1': num1, 'num2': num2})


# 模板继承
def main(request):
    return render(request, 'myApp/main.html')


def detail2(request):
    return render(request, 'myApp/detail.html')


# CSRF
def postfile(request):
    return render(request, 'myApp/postfile.html')


def showinfo(request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('passwd')
    print(password)
    return render(request, 'myApp/showinfo.html', {
        'username': username,
        'password': password
    })


# 验证码
def captcha(request):
    import os
    import random
    # import base64
    from io import BytesIO
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont

    def random_color():
        c1 = random.randint(0, 255)
        c2 = random.randint(0, 255)
        c3 = random.randint(0, 255)
        return c1, c2, c3

    def generate_picture(width=120, height=35):
        image = Image.new('RGB', (width, height), random_color())
        return image

    def random_str():
        '''
        获取一个随机字符, 数字或小写字母
        :return:
        '''
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(97, 122))
        random_char = random.choice([random_num, random_low_alpha])
        return random_char

    def draw_str(count, image, font_size):
        """
        在图片上写随机字符
        :param count: 字符数量
        :param image: 图片对象
        :param font_size: 字体大小
        :return:
        """
        draw = ImageDraw.Draw(image)
        # 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
        font_file = r'C:\Windows\Fonts\Adobe Arabic\AdobeArabic-Regular.otf'
        font = ImageFont.truetype(font_file, size=font_size)
        temp = []
        for i in range(count):
            random_char = random_str()
            draw.text((10 + i * 30, -2),
                      random_char,
                      random_color(),
                      font=font)
            temp.append(random_char)

        valid_str = "".join(temp)  # 验证码
        return valid_str, image

    def noise(image, width=120, height=35, line_count=3, point_count=20):
        '''

        :param image: 图片对象
        :param width: 图片宽度
        :param height: 图片高度
        :param line_count: 线条数量
        :param point_count: 点的数量
        :return:
        '''
        draw = ImageDraw.Draw(image)
        for i in range(line_count):
            x1 = random.randint(0, width)
            x2 = random.randint(0, width)
            y1 = random.randint(0, height)
            y2 = random.randint(0, height)
            draw.line((x1, y1, x2, y2), fill=random_color())

            # 画点
            for i in range(point_count):
                draw.point(
                    [random.randint(0, width),
                     random.randint(0, height)],
                    fill=random_color())
                x = random.randint(0, width)
                y = random.randint(0, height)
                draw.arc((x, y, x + 4, y + 4), 0, 90, fill=random_color())

        return image

    image = generate_picture()
    valid_str, image = draw_str(4, image, 35)
    request.session['captcha'] = valid_str
    # print(valid_str)
    # print(type(valid_str))
    image = noise(image)

    f = BytesIO()
    image.save(f, 'png')  # 保存到BytesIO对象中, 格式为png
    return HttpResponse(f.getvalue(), 'image/png')


def captchafile(request):
    flag = request.session.get('flag', 'True')
    str = ''
    if flag == False:
        str = '请重新输入'
    request.session.clear()
    return render(request, 'myApp/captchafile.html', {'flag': str})


def verifycaptcha(request):
    code1 = request.POST.get('verifycaptcha').upper()
    code2 = request.session['captcha'].upper()
    if code1 == code2:
        return render(request, 'myApp/success.html')
    else:
        request.session['flag'] = False
        return redirect('/sunck/captchafile/')


# 文件上传
def uploadfile(request):
    return render(request, 'myApp/uploadfile.html')


import os
from django.conf import settings


def savefile(request):
    # print("****")
    # print(request.method)
    # print(request.FILES)
    # print(type(request.FILES))
    if request.method == 'POST':
        f = request.FILES['file']
        # print(f)
        # print(f.name)
        # print(type(f))
        # 文件在服务器的路径
        filePath = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(filePath, 'wb') as fp:
            # 以文件流的形式一段一段写入
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")


from django.core.paginator import Paginator
# 分页
def studentpage(request, pageid):
    # 所有学生列表
    allList = Students.stuObject2.all()

    paginator = Paginator(allList, 2)
    page = paginator.page(pageid)

    return render(request, 'myApp/studentpage.html', {'students': page})


# 富文本
def edit(request):
    return render(request, 'myApp/edit.html')


# celery
import time


def celery(request):
    print("sunck is good man")
    time.sleep(5)
    print("sunck is nice man")
    return render(request, 'myApp/celery.html')


# CBV
from django.views import View


class Login(View):
    def get(self, request):
        return HttpResponse("GET 方法")

    def post(self, request):
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "runoob" and pwd == "123456":
            return HttpResponse("POST 方法")
        else:
            return HttpResponse("POST 方法 1")
