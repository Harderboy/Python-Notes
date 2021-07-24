# Django admin

Django 提供了基于 web 的管理工具。

Django 自动管理工具是 django.contrib 的一部分。你可以在项目的 `settings.py` 中的 INSTALLED_APPS 看到它：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApp',
]
```

django.contri b是一套庞大的功能集，它是 Django 基本代码的组成部分。

## admin后台类操作数据库

- 位置：具体 app 目录下的 `admin.py`

- 在 `admin.py` 中同时引进多个类：`admin.site.register([Test, Contact, Tag])`

- 自定义管理页面，来取代默认的页面，管理页面的显示格式

  定义了一个 GradesAdmin 类，此类继承 admin.ModelAdmin，用以说明管理页面的显示格式

    ```python
    # 自定义表单
    class GradesAdmin(admin.ModelAdmin):
        # 加两行
        inlines = [StudentsInfo]
        # 列表页属性
        # 显示字段
        list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
        # 过滤字段，过滤器
        list_filter = ['gname']
        # 搜索框中搜索字段
        search_fields = ['gname']
        # search_fields = ('gname',)
        # 列表分页
        list_per_page = 5

        # 属性的先后顺序
        # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']
        # fields、fieldsets不能同时使用
        # 将输入栏分块，其中增加、修改页属性显示格式，涉及 CSS 格式
        # 分为了num和base两部分，num部分显示ggirlnum、gboynum两个字段
        # base部分显示gname、gdate、isDelete三个字段
        fieldsets = [("num", {
            "fields": ['ggirlnum', 'gboynum']
        }), ("base", {
            "fields": ['gname', 'gdate', 'isDelete']
        })]
    ```

    注册的时候，需要将它们一起注册
  `admin.site.register(Grades, GradesAdmin)`

  - 其他详见 [admin.py 文件](./myproject/myApp/admin.py)

  - 一些写法存疑，类似 `search_fields = ['gname']` 用列表还是元组
    - 验证得到：`'search_fields' must be a list or tuple.`，二者皆可
    - 注意点单个元素的元组，须在单个元素后面添加 `,`，比如
      `search_fields = ('gname',)`