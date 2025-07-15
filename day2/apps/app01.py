from fastapi import APIRouter

user = APIRouter()

@user.get('/user/{user_id}')
def select(user_id:int):
    print("user_id",user_id)
    print(type(user_id))
    return {"userid":user_id}
