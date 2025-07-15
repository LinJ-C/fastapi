from fastapi import APIRouter
from typing import Union,Optional

boss = APIRouter()

@boss.get('/job/{kd}')
async def get_job(kd,xl:Union[None,str]=None,gj:Optional[str]=None): ##没有默认值则查询参数必填
    #数据库查询
    return {"kd":kd,
            "xl":xl,
            "gj":gj}
