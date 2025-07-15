from fastapi import APIRouter
from models import *
from pydantic import BaseModel, field_validator
from typing import Union,Optional
from fastapi.exceptions import HTTPException

student_api = APIRouter()

@student_api.get('/')
async def get_all_students():
    students = await Student.all()   # Queryset：[Student(), Student(), Student()]
    
    #过滤查询 filter
    # Student.filter(name='linwar')
    # Student.filter(cla_id=1)
    # Student.get(id=1)   返回的是model 对象
    # Student.filter(sno __gt =2001)   学号大于2001的数据
    # Student.filter(sno __in =[2001,2002])   学号在之中的
    # Student.filter(sno __range =[1,10000])   学号xxx范围之中
    # Student.filter(sno __range =[1,10000])   学号xxx范围之中
    # Student.all().values('name') select name from student [{},{},{}]
    

    return {"msg":students}

### 一对多查询 和 多对多查询
@student_api.get('/all')
async def get_one_students():
    
    #一对多查询，查学生和班级的信息
    linwar = await Student.get(name='linwar007')
    clas1 = await linwar.clas.values('name')
    print(clas1['name'])

    ## 使用prefetch_related
    # linwar = await Student.filter(name='linwar007').prefetch_related('clas').first()
    # print(linwar.clas.name)
    # return {
    #     "stu_name":linwar.name,
    #     "clas_name":linwar.clas.name
    # }
    ##集合情况怎么查 __ （双下杠）跨表查询
    # stus = await Student.all().values('name','clas__name')


    ## 多对多查询
    #print(await linwar.courses.all().values('name','teacher__t_name'))
    
    #stus = await Student.all().values('name','clas__name','courses__name')
    
    #prefetch_related 方法
    # students = await Student.all().prefetch_related(
    # "courses__teacher"  # 双下划线表示跨关系
    # )

    # # 访问数据
    # for student in students:
    #     for course in student.courses:
    #         print(f"学生 {student.name} 的课程 {course.name} 由 {course.teacher.t_name} 教授")
    return {'add':'111'}

    ## 原生sql
    # query = """
    #             SELECT 
    #                 s.id as student_id,
    #                 s.name as student_name,
    #                 json_group_array(
    #                     json_object(
    #                         'course_id', c.id,
    #                         'course_name', c.name,
    #                         'teacher_name', t.name
    #                     )
    #                 ) as courses
    #             FROM student s
    #             JOIN student_course sc ON s.id = sc.student_id
    #             JOIN course c ON sc.course_id = c.id
    #             JOIN teacher t ON c.teacher_id = t.id
    #             GROUP BY s.id
    #         """
    # students = await Student.raw(query)

class Student_in(BaseModel):
    name:str 
    pwd :str
    sno :int
    #一对多
    clas:Optional[int]=None
    #多对多
    courses: list[int] = []

    @field_validator('sno')
    def valitor_sno(cls, value):
        assert value >1000 and value < 20000, '学号要在1000和20000之间'
        
        return value

@student_api.post('/')
async def add_students(studentIn: Student_in):
    #插入到数据库
    # 方式一
    # student = Student(name=studentIn.name, pwd=studentIn.pwd, sno=studentIn.sno, clas_id = studentIn.clas)
    # await student.save()

    # 方式二
    student = await Student.create(name=studentIn.name, pwd=studentIn.pwd, sno=studentIn.sno, clas_id = studentIn.clas)
    
    # 多对多的关系绑定 #多对多关系必须用实例去操作
    choose_teacher = await Teacher.filter(id__in = studentIn.teacher)
    await student.teachers.add(*choose_teacher)

    choose_courses = await Course.filter(id__in = studentIn.course)
    await student.courses.add(*choose_courses)
    

    return {"msg":"添加一个学生信息"}


@student_api.put('/{student_id}')
async def updata_students(student_id:str,studentIn:Student_in):
    # data = studentIn.model_dump()
    # print(data)
    # courses = data.pop("courses")
    # clas_in = data.pop("clas")

    # await Student.filter(id=int(student_id)).update(**data) ## **data 是打散 不需要一个一个对应写，必须给数据库字段对应

    # edit_student = await Student.get(id__in=int(student_id))

    # choose_courses = await Course.filter(id__in=courses)
    # choose_clas = await Course.filter(id__in=clas_in)

    # await edit_student.courses.clear()
    # await edit_student.courses.add(*choose_courses)
    # await edit_student.clas.clear()
    # await edit_student.clas.add(*choose_clas)
    
    return {f"msg":"修改{student_id}所有学生信息"}

@student_api.delete('/{student_id}')
async def delect_students(student_id:int):
    delcount = await Student.filter(id=student_id).delete()
    if not delcount:
        raise HTTPException(status_code='404',detail=f'主键id为{student_id}的学生不存在')
    
    return {f"msg":"成功删除{student_id}的学生信息!"}
