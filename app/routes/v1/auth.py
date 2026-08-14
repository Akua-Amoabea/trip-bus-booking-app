from fastapi import APIRouter, Depends, HTTPException

from app.config.database import get_db
from app.schemas.users import  GetUserSchema, LoginUserSchema
from sqlalchemy.orm import Session

from app.models.users import User
from app.core.core import  verify_password



auth_router = APIRouter(
    tags= ["auth"],
    prefix="/v1/auth"
)

@auth_router.post("/login", response_model=GetUserSchema)
async def login_user(user: LoginUserSchema,db: Session=Depends(get_db)):
    
    trimmed_email = user.email.strip()
    current_user = db.query(User).filter(User.email == trimmed_email).first()
    
    if not current_user:
        HTTPException(status_code=404, detail='User doesnt have an account')
    
    verified =  verify_password(password=user.password, hashed_password=current_user.password)   
    
    if not verified:
        HTTPException(status_code=404, detail="InCorrect Password")
        
    return current_user 