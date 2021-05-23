from sqlalchemy import Column, Integer, String
from .database import Base

class SPUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username=Column(String)
    pw=Column(String)
    token=Column(String)
    credits=Column(Integer)

class Ship(Base):
    __tablename__ = "ships"
    id = Column(Integer, primary_key=True, index=True)
    shipname=Column(String)
    # token=Column(str)
    # fueltank=Column(int)
    # hull=Column(int)
    # cargoslots=Column(int)
    # posSolSystem=Column(str)
    # x=Column(int)
    # y=Column(int)

# https://fastapi.tiangolo.com/tutorial/extra-models/