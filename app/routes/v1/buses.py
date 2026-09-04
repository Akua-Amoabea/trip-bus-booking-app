from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.buses import CreateBusSchema, GetBusSchema
from app.config.database import get_db
from app.models.buses import Bus
from app.models.seats import Seat
from app.models.users import User
from app.services.auth import get_current_user


bus_router = APIRouter(
    prefix="/v1/buses",
    tags=["Buses"]
)


@bus_router.post("", response_model= GetBusSchema)
async def add_bus(bus:CreateBusSchema, db:Session=Depends(get_db)):
    
    with db.begin():
        get_bus = db.query(Bus).filter(Bus.bus_number == bus.bus_number).first()
        
        if get_bus:
            raise HTTPException(
                status_code=409,
                detail="Bus already exists"
            )
            
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
            
        
        db.refresh(new_bus)
            
    return new_bus


@bus_router.get("", response_model= list[GetBusSchema])
async def get_buses(db:Session=Depends(get_db), current_user: User=Depends(get_current_user)):
   all_buses= db.query(Bus).all()
   
   if not all_buses:
       raise HTTPException(status_code=404, detail="No buses found")
   
   return all_buses




       