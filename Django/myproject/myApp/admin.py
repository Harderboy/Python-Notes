from django.contrib import admin

# Register your models here.
from .models import Grades, Students


# admin.StackedInline
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2


# 注册
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
    # 列表分页
    list_per_page = 5

    # 添加、修改页属性
    # 属性的先后顺序
    # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']
    # fields、fieldsets不能同时使用
    fieldsets = [("num", {
        "fields": ['ggirlnum', 'gboynum']
    }), ("base", {
        "fields": ['gname', 'gdate', 'isDelete']
    })]


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
