from sqlalchemy.orm import Session
import models
from auth import hash_password

def create_user(db:Session,username:str,password:str):
    user=models.User(username=username,password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user(db:Session,username:str):
    return db.query(models.User).filter(models.User.username==username).first()

def create_predictions(db:Session,text,result,user_id):
    prediction=models.Predictions(user_id=user_id,text=text,result=result)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction