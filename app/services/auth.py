from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.core.core import verify_token
from app.models.users import User


def get_current_user(token:str, db:Session):
    payload = verify_token(token=token)
    user_id = payload.get("sub")
    
    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
        
    
    user = db.query(User).filter(
        User.uuid == int(user_id)
    ).first()
    

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user
        
        
    