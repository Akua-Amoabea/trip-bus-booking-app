from fastapi import APIRouter, Depends

from app.schemas.bookings import  CreateBookingsSchema, GetBookingsSchema
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.selected_seats import GetSelectedSeatSchema, SelectedSeatSchema
from app.schemas.luggages import AddLuggagesSchema, GetLuggagesSchema
from app.models.selected_seats import SelectedSeat
from app.models.bookings import Booking
from app.models.luggages import Luggage


bookings_router = APIRouter(
    prefix="/v1/bookings",
    tags=['bookings']
)


@bookings_router.post("", response_model=GetBookingsSchema)
async def add_new_bookings(bookings:CreateBookingsSchema, db: Session=Depends(get_db)):
    
    new_luggages = None
    
    with db.begin():
        new_bookings = Booking(
            route_uuid=bookings.route_uuid,
            user_uuid=bookings.user_uuid
        )
        
        db.add(new_bookings)
        db.flush()
        
        if bookings.luggages:
                new_luggages = Luggage(
                 booking_uuid=new_bookings.uuid,
                 number_of_luggages=bookings.luggages.number_of_luggages,
                 weight_of_luggages=bookings.luggages.weight_of_luggages   
                )
                
                db.add(new_luggages)
                db.flush()
                
                           
        for seats_uuid in bookings.selected_seats:
            
            new_selected_seats= SelectedSeat(
                seat_uuid=seats_uuid,
                route_uuid=bookings.route_uuid,
                booking_uuid=new_bookings.uuid   
            )
                  
            
            db.add(new_selected_seats)
            
        
        all_seats = db.query(SelectedSeat).filter(SelectedSeat.booking_uuid == new_bookings.uuid).all()
        
    return GetBookingsSchema(
        uuid=new_bookings.uuid,
        route_uuid=new_bookings.route_uuid,
        user_uuid=new_bookings.user_uuid,
        selected_seats=[GetSelectedSeatSchema(
            uuid=seat.uuid,
            seat_uuid=seat.seat_uuid,
        )
        for seat in all_seats                
                        ],
        lugggages=(
            GetLuggagesSchema(
            uuid=new_luggages.uuid,
            number_of_luggages=new_luggages.number_of_luggages,
            weight_of_luggages=new_luggages.weight_of_luggages,
        )
        if new_luggages
        else None
        )
    )    
        
   
        
    
      
          
          
         
      
      
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    