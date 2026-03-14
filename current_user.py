from jose import jwt
import crud
from auth import SECRET_KEY,ALGORITHM
from sqlalchemy.orm import Session
from database import get_db
from fastapi import Depends,HTTPException


def get_current_user(token:str,db:Session=Depends(get_db)):
    token_decoded=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    username=token_decoded.get('sub')
    user=crud.get_user(db,username)

    if not user:
        raise HTTPException(status_code=401)
    return user