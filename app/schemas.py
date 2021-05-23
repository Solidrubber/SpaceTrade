from pydantic import BaseModel
from typing import Optional


class SPUser(BaseModel):
    username: str
    token: Optional[str] = 'dkdkdk9339do3o'
    pw: str
    credits: int = 10000