from pydantic import BaseModel
from typing import Optional


class SPUser(BaseModel):
    username: str
    token: Optional[str] = 'dkdkdk9339do3o'
    pw: str
    credits: int = 10000

class Ship(BaseModel):
    shipname: str
    token: Optional['str'] = 'ship9ß2mdi32033'
    fueltank: int = 25
    hull: int = 0
    cargoslots: int = 10
    posSolSystem: str
    x: int
    y: int
