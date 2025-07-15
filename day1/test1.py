from datetime import datetime
from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id:int
    name:str='linwar'
    timestamp: datetime
    dimensions: List[int] =[]


m = User(id='123',timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
#> (10, 20)
print(m.dict())