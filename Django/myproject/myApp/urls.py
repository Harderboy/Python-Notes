from django.conf.urls import url
# from django.urls import path
from . import views

urlpatterns = [
    url('^$', views.index),
    # path(r'', views.index),
    # path('<int:num>/', views.detail)
    # url(r'^(\d+)/$', views.vote),
    url(r'^(\d+)$', views.vote),
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
]
