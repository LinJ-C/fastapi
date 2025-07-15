from fastapi import APIRouter

shop = APIRouter()

@shop.post('/car')
def car():
    return {"car":"这是汽车接口"}

@shop.post('/food')
def food():
    return {"food":"这是食品接口"}