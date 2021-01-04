from django.db import models


# 一个模型类在数据库中对应一张数据表
# 使用模型类进行增删改查操作
# Create your models here.
# 不用创建主键，会自动生成且递增
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    # admin后台将每个Grades对象显示为：Grades object
    # 解决：重写__str__方法
    def __str__(self):
        # return "%s-%d-%d" % (self.gname, self.ggirlnum, self.gboynum)
        return self.gname

    # 模型的元数据即“所有不是字段的东西”，比如排序选项（ ordering ），数据库表名（ db_table，这些都不是必须的
    # class Meta:
    #     # ordering = ['id']
    #     db_table = "grades"


# 自定义管理器 `Manager`类
# 修改管理器返回的原始查询集， 重写get_quertset()方法
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,
                     self).get_queryset().filter(isDelete=False)

    def createStudents(self, name, age, gender, content, grade, isD=False):
        # 创建一个Students对象
        stu = self.model()
        # print(stu)
        # print(type(stu))
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontent = content
        stu.sgrade = grade
        return stu


class Students(models.Model):
    # 自定义模型管理器
    stuObject = models.Manager()
    stuObject2 = StudentsManager()
    # 没有定义模型管理器时，获取所有Students对象：Students.objects.all()
    # 定义后 Students.stuObject2.all()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    # sage = models.IntegerField(do_column="age")
    scontent = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)

    # python manage.py shell中操作
    # Students对象sgrade赋值
    # s = Students()
    # g = Grades()
    # s.sgrade = g
    # 保存数据：s.save()
    def __str__(self):
        return self.sname

    # lastTime = models.DateTimeField(auto_now=True)
    # createTime = models.DateTimeField(auto_created=True)
    # class Meta:
    #     # ordering = ['id']
    #     db_table = "students"

    # 定义一个类方法创建对象，添加@classmethod 表明以下方法为类方法
    # 不加@classmethod，def createStudents(Students):
    @classmethod
    def createStudents(cls, name, age, gender, content, grade, isD=False):
        stu = cls(sname=name,
                  sage=age,
                  sgender=gender,
                  scontent=content,
                  sgrade=grade,
                  isDelete=isD)
        return stu

    def getName(self):
        return self.sname


from tinymce.models import HTMLField


class Text(models.Model):
    str = HTMLField()
