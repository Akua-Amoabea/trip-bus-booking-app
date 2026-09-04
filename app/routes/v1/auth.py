from fastapi import APIRouter, Depends, HTTPException

from app.config.database import get_db
from app.schemas.users import LoginUserSchema
from sqlalchemy.orm import Session

from app.models.users import User
from app.core.core import  create_access_token, create_refresh_token, verify_password, verify_refresh_token
from app.services.otp import get_otp_code, save_otp_code, verify_otp_code
from app.services.email import send_verification_email



auth_router = APIRouter(
    tags= ["Auth"],
    prefix="/v1/auth"
)

@auth_router.post("/login")
async def login_user(user: LoginUserSchema,db: Session=Depends(get_db)):
    
    trimmed_email = user.email.strip()
    current_user = db.query(User).filter(User.email == trimmed_email).first()
    
    if not current_user:
        raise HTTPException(status_code=401, detail='User doesnt have an account')
    
    verified = verify_password(password=user.password, hashed_password=current_user.password)   
    
    if not verified:
        raise HTTPException(status_code=401, detail="InCorrect Password")
    
    
    if not current_user.is_verified:
        raise HTTPException(status_code=401, detail="User not verified")
        
        
    access_token = create_access_token(
            data={
                "sub": str(current_user.uuid),
                "email": current_user.email
            }
        )
    
    refresh_token = create_refresh_token(
            data={
                "sub": str(current_user.uuid)
            }
        )
    
    return {
            "message": "Email verified successfully",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        } 



@auth_router.post("/verify_otp")
async def verify_otp(otp_code: str, email:str, db:Session=Depends(get_db)):
    trimmed_email = email.strip()

    user = db.query(User).filter(User.email == trimmed_email).first()
    
    if not user:
        raise HTTPException(status_code=401, detail='User doesnt have an account')

    is_verified = verify_otp_code(otp=otp_code, email=user.email)
    
    if not is_verified:
        raise HTTPException(status_code=401, detail='Incorrect OTP code')
        
    user.is_verified = True
    
    db.commit()
    db.refresh(user)
    
    access_token = create_access_token(
        data={
            "sub": str(user.uuid),
            "email": user.email
        }
    )

    refresh_token = create_refresh_token(
        data={
            "sub": str(user.uuid)
        }
    )

    return {
        "message": "Email verified successfully",
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@auth_router.post("/resend_otp")
async def resend_otp_code(email:str, db:Session=Depends(get_db)):
    
    trimmed_email = email.strip()
    
    user = db.query(User).filter(User.email == trimmed_email).first()
        
    if not user:
        raise HTTPException(status_code=404, detail='User doesnt have an account')
    
    if user.is_verified:
        raise HTTPException(
            status_code=400,
            detail="Email is already verified"
        )
    
    otp = get_otp_code()
    save_otp_code(email=user.email, otp=otp)
    send_verification_email(email=user.email, first_name=user.first_name, code=otp)
    
    return "OTP has been sent to your email"
            

@auth_router.post("/refresh_token")
async def get_new_access_token(refresh_token: str, db: Session=Depends(get_db)):       
    payload = verify_refresh_token(refresh_token)
    user = db.query(User).filter(User.id == payload.get("sub")).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    access_token = create_access_token(
        data={
            "sub": str(user.uuid),
            "email": user.email
        }
    )
    return {
        "access_token": access_token,
        "type": "bearer"
    }    
        