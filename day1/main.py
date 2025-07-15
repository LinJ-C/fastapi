from fastapi import FastAPI
import uvicorn
from apps.app01.urls import shop
from apps.app02.urls import user

app = FastAPI()

app.include_router(shop,prefix='/shop',tags=['这是一个购物接口'])
app.include_router(user,prefix='/user',tags=['这是一个用户接口'])

if __name__ == '__main__':
    uvicorn.run('main:app',port=8080, reload=True)