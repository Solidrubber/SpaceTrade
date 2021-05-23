from fastapi import APIRouter

router = APIRouter()

fake_items_db = {"Schiff": {"name": "Kunoabgsoffen"}, "SchiffII": {"name": "Blubbe"}}

@router.get("/ship")
async def read_items():
    return fake_items_db