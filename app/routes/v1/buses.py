from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.buses import CreateBusSchema, GetBusSchema
from app.config.database import get_db
from app.models.buses import Bus
from app.models.seats import Seat



bus_router = APIRouter(
    prefix="/v1/buses",
    tags=["buses"]
)


@bus_router.post("", response_model= GetBusSchema)
async def add_bus(bus:CreateBusSchema, db:Session=Depends(get_db)):
    
    with db.begin():
        new_bus = Bus(
        bus_number=bus.bus_number,
        capacity=bus.capacity,
        with_ac=bus.with_ac     
        )
        
        db.add(new_bus)
        db.flush()
       
        
        for number in range(1, new_bus.capacity+1):
            new_seat = Seat(
            seat_number=number,
            bus_uuid=new_bus.uuid      
            )
            db.add(new_seat)
            
        db.commit()
        db.refresh(new_bus)
            
    return new_bus


@bus_router.get("", response_model= list[GetBusSchema])
async def get_bus(db:Session=Depends(get_db)):
   all_buses= db.query(Bus).all()
   
   return all_buses


@bus_router.get("/{id}", response_model=GetBusSchema) 
async def get_bus_by_id(uuid: str, db: Session=Depends(get_db)):
    bus = db.query(Bus).filter(Bus.uuid == uuid).first()
    if not bus:
        HTTPException(status_code=404,
                      detail="Bus not Found")
    
    return bus

       