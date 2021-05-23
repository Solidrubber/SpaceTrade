from fastapi import APIRouter

router = APIRouter()

fake_items_db = {"Sonne": {"name": "Sonne"}, "Soliana1": {"name": "Nicht unsere Sonne"}}

@router.get("/solsytems")
async def read_items():
    return fake_items_db