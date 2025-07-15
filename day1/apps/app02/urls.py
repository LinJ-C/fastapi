from fastapi import APIRouter

user = APIRouter()

@user.post('/login')
def login():
    return {"userid":"linwar"}

@user.post('/regin')
def regin():
    return {"passwd":"123"}