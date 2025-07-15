from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get")
def get_test():
    return {"method": "get方法"}


@app.post(
    "/items/{item_id}",
    # response_model=Item,
    # status_code=status.HTTP_200_OK,
    tags=["AAA"],
    summary="this is summary",
    description="this is description",
    response_description= "this is response_description",
    deprecated=True,
)
def test():
    return {"items":11}


@app.put("/put",)
def put_test():
    return {"method": "put方法"}


@app.delete("/delete")
def delete_test():
    return {"method": "delete方法"}



if __name__ == '__main__':
    uvicorn.run('路径操作:app',port=8080, reload=True)