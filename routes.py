from fastapi import APIRouter,Depends,Request
import schemas
import crud
from sqlalchemy.orm import Session
from database import get_db
from auth import verify_password,create_access_token
from current_user import get_current_user
from ml_model import predict

from ratelimiter import limiter


router=APIRouter()

@router.post('/register')
async def register(user:schemas.UserCreate,db:Session=Depends(get_db)):
    existing_user = crud.get_user(db, user.username)

    if existing_user:
        return {"error": "username already exists"}
    return crud.create_user(db,user.username,user.password)

@router.post('/login')
@limiter.limit('5/minute')
async def login(request:Request,user:schemas.UserCreate,db:Session=Depends(get_db)):
    db_user=crud.get_user(db,user.username)

    if not db_user:
        return {'error':'invalid user'}
    if not verify_password(user.password,db_user.password):
        return{'error':'invalid paassword'}
    
    token=create_access_token({'sub':db_user.username})
    return {'access_token':token,'token_type':'bearer'}

@router.post('/predict')
@limiter.limit('5/minute')
async def predict_text(request:Request,data:schemas.PredictionRequest,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    
    result=predict(data.text)
    crud.create_predictions(db,data.text,result,current_user.id)
    return {'prediction':result}