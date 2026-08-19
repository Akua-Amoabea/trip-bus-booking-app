from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.locations import CreateLocationSchema, GetLocationSchema
from app.models.locations import Location


location_router = APIRouter(
    prefix="/v1/locations",
    tags=["locations"]
)


@location_router.post("", response_model=GetLocationSchema)
async def add_location(location:CreateLocationSchema, db: Session=Depends(get_db)):
    new_location = Location(
        name=CreateLocationSchema.name   
    )
    
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    
    return new_location
    