from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from app.core.core import verify_token
from app.models.users import User
from app.config.database import get_db
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db:Session= Depends(get_db)):
    
    token = credentials.credentials
    payload = verify_token(token=token)
    user_id = payload.get("sub")
    
    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
        
    
    user = db.query(User).filter(
        User.uuid == user_id
    ).first()
    

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user
        
        
    