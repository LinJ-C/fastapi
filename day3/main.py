from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from config import Config
from api.student import student_api

app = FastAPI()
register_tortoise(app,config=Config)

app.include_router(student_api,prefix='/student',tags=['this is a student api'])

if __name__ == '__main__':
    uvicorn.run('main:app',port=8080, reload=True)