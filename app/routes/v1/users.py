from fastapi import APIRouter, Depends, HTTPException

from app.config.database import get_db
from app.schemas.users import CreateUserSchema, GetUserSchema
from sqlalchemy.orm import Session

from app.models.users import User
from app.core.core import hash_password
from app.services.otp import get_otp_code, save_otp_code
from app.services.email import send_verification_email



user_router = APIRouter(
    prefix="/v1/users",
    tags=["users"]
)


@user_router.post("",response_model=GetUserSchema)
async def create_user(user:CreateUserSchema, db:Session=Depends(get_db)):
   valid_user =  db.query(User).filter(User.email == user.email).first()
   if valid_user:
       raise HTTPException(
           status_code=409,
           detail="Email already exists"
       )
       
   new_user = User(
       first_name = user.first_name,
       last_name= user.last_name,
       email= user.email,
       password=hash_password(password=user.password),
       profile_picture=user.profile_picture,
       is_verified=False
          
   )
   
   otp = get_otp_code()
   save_otp_code(email=user.email, otp=otp)
   send_verification_email(email=user.email, first_name=user.first_name, code=otp)
       
   db.add(new_user)
   db.commit()
   db.refresh(new_user) 
   
   return new_user 
       

   
        
       
   

  