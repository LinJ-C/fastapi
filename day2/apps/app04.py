from fastapi import APIRouter,Form


rein = APIRouter()

@rein.post('/regin')
async def regin(username:str = Form(), password:str =Form()):
    print(f"usernmae:{username},\n password:{password}")
    return {"username":username}
    #数据库查询
    
