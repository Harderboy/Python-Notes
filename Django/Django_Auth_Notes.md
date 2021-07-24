# Django auth

参考 [Django 用户认证（Auth）组件](https://www.runoob.com/django/django-auth.html)

## 装饰器的使用

设置装饰器，给需要登录成功后才能访问的页面统一加装饰器。

```python
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return HttpResponse("index页面。。。")
```
