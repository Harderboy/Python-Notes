from django.contrib import admin

# Register your models here.
from .models import Grades, Students


# Grades是Students的外键，有外部参考的关系
# 而在默认的页面显示中，将两者分离开来，无法体现出两者的从属关系。我们可以使用内联显示，让 Students 附加在 Grades 的编辑页面上显示
# admin.StackedInline 垂直
# 水平，类表格式
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2


# 自定义表单
class GradesAdmin(admin.ModelAdmin):
    # 内联(Inline)显示
    # 加两行
    inlines = [StudentsInfo]
    # 列表页属性
    # 显示字段
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    # 过滤字段，过滤器
    list_filter = ['gname']
    # 搜索框中搜索字段
    # search_fields = ['gname']
    search_fields = ('gname',)
    # 列表分页
    list_per_page = 2

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


# 定义了一个 GradesAdmin 类，此类继承admin.ModelAdmin，用以说明管理页面的显示格式。
admin.site.register(Grades, GradesAdmin)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'

    # 设置页面列的名称
    gender.short_description = '性别'
    list_display = [
        'pk', 'sname', 'sage', gender, 'scontent', 'sgrade', 'isDelete'
    ]
    list_per_page = 3
    # “执行动作”的位置
    actions_on_top = False
    actions_on_bottom = True

# 改用装饰器
# admin.site.register(Students, StudentsAdmin)


from .models import Text

admin.site.register(Text)
