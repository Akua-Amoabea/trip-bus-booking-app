from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.buses import CreateBusSchema
from app.models.buses import Bus
from app.config.database import get_db

admin_router = APIRouter(
    tags= ["buses"],
    prefix="/v1/buses"
)



@admin_router.post("")
async def add_buses(bus: CreateBusSchema, db: Session=Depends(get_db())):
    new_bus = Bus(
    leaving_time=bus.leaving_time,
    destination_time=bus.destination_time,
    with_ac=bus.with_ac,
    location=bus.location,
    destination=bus.destination,
    price=bus.price,
    leaving_date=bus.leaving_date
)

    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)
        
