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
    url(r'^students/$', views.students),
    url(r'^grades/(\d+)/$', views.gradesStudents)
]
