from app.routers import ship
from fastapi import FastAPI

from pydantic import BaseModel
from .routers import user, items, solsystem, ship, game


app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hallo Welt"}


app.include_router(user.router)
app.include_router(items.router)
app.include_router(solsystem.router)
app.include_router(ship.router)
app.include_router(game.router)