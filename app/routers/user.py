from fastapi import Depends, APIRouter
from typing import Optional
from .. import schemas, models
from ..database import engine, SessionLocal
from sqlalchemy.orm import Session

#app = FastAPI()
router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#@app.post('/user')
@router.post('/user', tags=["users"])
def create(request: schemas.SPUser, db : Session = Depends(get_db)):
    new_user = models.SPUser(username=request.username, pw = request.pw, token=request.token, credits=request.credits)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    #return {f'creating user {request.username} mit Token {request.token} Credits: {request.credits} '}


# @app.get("/user")
# async def showUser(limit: int = 10, published: bool = True, sort: Optional[str] = None):
#     # Übergabeparams prüfen: /user?limit=100?published=True?sort
#     if published:
#         return {"message": f'{limit} user published {published}'}
#     else:
#         return {"message": f'{limit} usernames published {published}'}

# @app.get("/user/{id}")
# async def getUserById(id: int):
#     return {'data': id}

# @app.get("/user/{id}/ships")
# async def getUserShipsById(id):
#     return {'Username': id, 'ships': 'schiffno1 - Scout'}
