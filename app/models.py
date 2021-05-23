from sqlalchemy import Column, Integer, String
from .database import Base

class SPUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username=Column(String)
    pw=Column(String)
    token=Column(String)
    credits=Column(Integer)