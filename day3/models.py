## 选课系统
from tortoise.models import Model
from tortoise import fields

class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description='姓名')
    pwd = fields.CharField(max_length=32, description='密码')
    sno = fields.IntField(description='学号')

    #一对多
    clas = fields.ForeignKeyField("models.Clas", related_name="students")
    #多对多
    courses = fields.ManyToManyField('models.Course',related_name='students')

class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description='班级')

class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description='课程')
    teacher = fields.ForeignKeyField('models.Teacher',related_name='course')
    addr = fields.CharField(max_length=32, description='教室', default='')

class Teacher(Model):
    id = fields.IntField(pk=True)
    t_name = fields.CharField(max_length=32, description='老师名字')
    pwd = fields.CharField(max_length=32, description='密码')
    tno = fields.IntField(description='教师编号')