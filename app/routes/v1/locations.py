from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.locations import CreateLocationSchema, GetLocationSchema
from app.models.locations import Location
from app.models.users import User
from app.services.auth import get_current_user


location_router = APIRouter(
    prefix="/v1/locations",
    tags=["Locations"]
)


@location_router.post("", response_model=GetLocationSchema)
async def add_location(location:CreateLocationSchema, db: Session=Depends(get_db)):
    
    get_location = db.query(Location).filter(Location.name == location.name).first()
    
    if get_location:
        raise HTTPException(
            status_code=409,
            detail="location already exists"
        )
    new_location = Location(
        name=location.name   
    )
    
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    
    return new_location
    


@location_router.get("", response_model=list[GetLocationSchema])
async def get_locations(db:Session=Depends(get_db), current_user :User = Depends(get_current_user)):
    user = db.query(User).filter(User.uuid == current_user.uuid).first()
        
    if not user:
            raise HTTPException(
                status_code=401,
                detail="User not authenticated"
            )
    all_locations = db.query(Location).all()  
    if not all_locations:
        raise HTTPException(
            status_code=404,
            detail="No location found"
        )
        
    return all_locations    
    