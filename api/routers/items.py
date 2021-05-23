from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}



@router.get("/items")
async def read_items():
    return fake_items_db


@router.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}