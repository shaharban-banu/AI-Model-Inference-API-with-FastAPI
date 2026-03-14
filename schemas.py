from pydantic import BaseModel

class UserCreate(BaseModel):
    username:str 
    password:str

# class Token(BaseModel):
#     access_token:str

class PredictionRequest(BaseModel):
    text:str

class PredictionResponse(BaseModel):
    result:str