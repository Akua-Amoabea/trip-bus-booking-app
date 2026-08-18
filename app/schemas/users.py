from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    profile_picture: str
       
    
class GetUserSchema(BaseModel):
    uuid: UUID
    email: EmailStr
    first_name:str
    last_name:str
    profile_picture:str
    created_time:datetime
    
 
class LoginUserSchema(BaseModel):
     email:str
     password:str
     
            
    
    
    
        