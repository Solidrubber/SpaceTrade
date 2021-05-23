from fastapi import Depends, APIRouter
from typing import Optional
from .. import schemas, models
from ..database import engine, SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

fake_items_db = {"Schiff": {"name": "Kunoabgsoffen"}, "SchiffII": {"name": "Blubbe"}}

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/ship")
async def read_items():
    return fake_items_db