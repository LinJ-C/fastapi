from fastapi import FastAPI
import uvicorn
from apps.app01 import user
from apps.app02 import boss
from apps.app03 import data
from apps.app04 import rein
from apps.app05 import file


app = FastAPI()

app.include_router(file,prefix='/file',tags=['文件上传'])
app.include_router(user,prefix='/shop',tags=['这是一个用户接口'])
app.include_router(boss,prefix='/boss',tags=['这是查询参数'])
app.include_router(data,prefix='/data',tags=['这是请求体参数'])
app.include_router(rein,prefix='/da',tags=['这是form表达'])



if __name__ == '__main__':
    uvicorn.run('main:app',port=8080, reload=True)