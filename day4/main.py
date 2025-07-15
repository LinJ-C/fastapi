from fastapi import FastAPI, Request, Response
import uvicorn
import time
app = FastAPI()


@app.middleware('http')
async def m2(request:Request, call_next):
    #请求代码块
    print("m2 请求数据")
    response = await call_next(request)

    response.headers['author'] = 'linwar'
    print('m2 响应数据')

    return response

@app.middleware('http')
async def m1(request:Request, call_next):
    #请求代码块
    # if request.client.host in ["127.0.0.1", ]:  # 黑名单
    #     return Response(content="visit forbidden")

    # if request.url.path in ["/user"]:
    #     return Response(content="visit forbidden")
    
    print("m1 请求数据")
    start = time.time()
    response = await call_next(request)

    print('m1 响应数据')
    end=time.time()
    response.headers['ProcessTimer'] = str(end-start)
    
    
    
    return response

@app.get('/user')
def find_user():
    time.sleep(2)
    return {"msg":"拿到用户信息"}


@app.get('/item')
def find_user():
    time.sleep(3)
    return {"msg":"拿到物品信息"}

if __name__ == '__main__':
    uvicorn.run('main:app',port=8080, reload=True)