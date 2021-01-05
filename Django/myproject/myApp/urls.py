from django.conf.urls import url
# from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # url('^$', views.index, name="index"),
    url('^$', views.index, name="index"),
    url(r'index.html', views.index1),
    # path(r'', views.index),
    # path('<int:num>/', views.detail)
    # url(r'^(\d+)/$', views.vote),
    url(r'^(\d+)/$', views.vote),
    url(r'^(\d+)/(\d+)/$', views.detail),
    url(r'^grades/$', views.grades),
    url(r'^grades2/$', views.grades2),
    url(r'^students/$', views.students),
    url(r'^students2/$', views.students2),
    url(r'^students3/$', views.students3),
    url(r'^students/(\d+)/$', views.stupage),
    url(r'^studentsearch/$', views.studentsearch),
    url(r'^grades/(\d+)/$', views.gradesStudents),
    url(r'^grades2/(\d+)/$', views.gradesStudents),
    url(r'^addstudent/$', views.addstudent),
    url(r'^addstudent2/$', views.addstudent2),

    url(r'^attribute/$', views.attribute),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),

    url(r'^showregist/$', views.showregist),
    url(r'^showregist/regist/$', views.regist),

    url(r'^showresponse/$', views.showresponse),
    url(r'^cookietest/$', views.cookietest),

    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),

    # url(r'homepage/$', views.homepage) 也是可以的
    url(r'^homepage/$', views.homepage),
    url(r'^login/$', views.login),
    url(r'^showhomepage/$', views.showhomepage),
    url(r'^quit/$', views.quit),

    url(r'^getstudent/$', views.getstudent),

    url(r'^good/(\d+)/(\d+)$', views.good, name="good"),

    url(r'^main/$', views.main),
    url(r'^detail2/$', views.detail2),

    url(r'^postfile/$', views.postfile),
    url(r'^showinfo/$', views.showinfo),

    url(r'^captcha/$', views.captcha),
    url(r'^captchafile/$', views.captchafile),
    url(r'^verifycaptcha/$', views.verifycaptcha),

    url(r'^uploadfile/$', views.uploadfile),
    url(r'^savefile/$', views.savefile),

    url(r'^studentpage/(\d+)/$', views.studentpage),

    url(r'^edit/$', views.edit),

    url(r'^celery/$', views.celery),

    url(r'^login2/$', views.Login.as_view()),
]
