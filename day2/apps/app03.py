from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date

data = APIRouter()

class Addr(BaseModel):
    province:str
    city:str



class User(BaseModel):
    id:int=Field(default=0,gt=0,lt=100)
    name:str = Field(pattern='^a') #正则验证 必须以a开头的字符串
    create_time:date
    friends:list[int]
    addr:Addr

    # 自定义函数验证方式
    @field_validator('name')
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name not alpha'
        return value
    
class Data(BaseModel):
    data:list[User]

@data.post('/')
async def get_job(user:User): 
    #数据库查询
    print(user.id)
    print(user.model_dump())

    return user

@data.post('/user')
async def get_data(data:Data):
    print(data.model_dump())
    return data