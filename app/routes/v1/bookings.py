from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.schemas.bookings import  CreateBookingsSchema, GetBookingsSchema, UpdateBookingsSchema
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.config.database import get_db
from app.schemas.selected_seats import GetSelectedSeatSchema
from app.schemas.luggages import  GetLuggagesSchema
from app.models.selected_seats import SelectedSeat
from app.models.bookings import Booking
from app.models.luggages import Luggage
from app.models.users import User
from app.services.auth import get_current_user


bookings_router = APIRouter(
    prefix="/v1/bookings",
    tags=['Bookings']
)

@bookings_router.post("", response_model=GetBookingsSchema)
async def add_new_bookings(bookings:CreateBookingsSchema, db: Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.uuid == current_user.uuid).first()
        
    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not authenticated"
        )
    
    
    new_luggages = None
    
    try:
    
        with db.begin():      
            new_bookings = Booking(
                route_uuid=bookings.route_uuid,
                user_uuid=bookings.user_uuid,
                status="active"
            )
            
            db.add(new_bookings)
            db.flush()
            
            if bookings.luggages:
                    luggage_price = 20 + ((bookings.luggages.number_of_luggages -1) * 15)
                    free_weight = 10
                    excess_weight = max(bookings.luggages.weight_of_luggages - free_weight, 0)
                    weight_fee = excess_weight * free_weight
                    total_fee = luggage_price + weight_fee
                    
                    new_luggages = Luggage(
                    booking_uuid=new_bookings.uuid,
                    number_of_luggages=bookings.luggages.number_of_luggages,
                    weight_of_luggages=bookings.luggages.weight_of_luggages,
                    price= total_fee
                    )
                    
                    db.add(new_luggages)
                    db.flush()
                    
                            
            for seats_uuid in bookings.selected_seats: 
                
                new_selected_seats= SelectedSeat(
                    seat_uuid=seats_uuid,
                    route_uuid=bookings.route_uuid,
                    booking_uuid=new_bookings.uuid,  
                )
                    
                
                db.add(new_selected_seats)
                
            db.flush()
            
            all_seats = db.query(SelectedSeat).filter(SelectedSeat.booking_uuid == new_bookings.uuid).all()
            
            print("Seats found:", all_seats)
            
        return GetBookingsSchema(
            uuid=new_bookings.uuid,
            route_uuid=new_bookings.route_uuid,
            user_uuid=new_bookings.user_uuid,
            status=new_bookings.status,
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
                price= new_luggages.price
            )
            if new_luggages
            else None
            )
        )    
            
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="One or more selected seats are already booked."
        )
            
        
        
@bookings_router.get("", response_model=list[GetBookingsSchema])
async def get_bookings(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    
    user = db.query(User).filter(User.uuid == current_user.uuid).first()
    
    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not authenticated"
        )

    all_bookings = db.query(Booking).all()
    
    if not all_bookings:
        raise HTTPException(
            status_code=404,
            detail="No Bookings Found"
        )

    for booking in all_bookings:

        selected_seats = (
            db.query(SelectedSeat)
            .filter(SelectedSeat.booking_uuid == booking.uuid)
            .all()
        )

        luggage = (
            db.query(Luggage)
            .filter(Luggage.booking_uuid == booking.uuid)
            .first()
        )

        return [
    GetBookingsSchema(
        uuid=booking.uuid,
        route_uuid=booking.route_uuid,
        user_uuid=booking.user_uuid,
        status=booking.status,

        selected_seats=[
            GetSelectedSeatSchema(
                uuid=seat.uuid,
                seat_uuid=seat.seat_uuid,
            )
            for seat in selected_seats
        ],

        lugggages=(
            GetLuggagesSchema(
                uuid=luggage.uuid,
                number_of_luggages=luggage.number_of_luggages,
                weight_of_luggages=luggage.weight_of_luggages,
                price=luggage.price,
            )
            if luggage
            else None
        ),
    )
    for booking in all_bookings
]
        

@bookings_router.patch("/{booking_uuid}/status", response_model=GetBookingsSchema)
async def change_status_of_booking(
    bookings: UpdateBookingsSchema,
    booking_uuid: UUID,
    db: Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    
    
    user = db.query(User).filter(User.uuid == current_user.uuid).first()
        
    if not user:
            raise HTTPException(
                status_code=401,
                detail="User not authenticated"
            )
    get_booking = (
        db.query(Booking)
        .filter(Booking.uuid == booking_uuid.uuid)
        .first()
    )

    if not get_booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    get_booking.status = bookings.status

    db.commit()
    db.refresh(get_booking)

    all_seats = (
        db.query(SelectedSeat)
        .filter(SelectedSeat.booking_uuid == get_booking.uuid)
        .all()
    )

    luggage = (
        db.query(Luggage)
        .filter(Luggage.booking_uuid == get_booking.uuid)
        .first()
    )

    return GetBookingsSchema(
        uuid=get_booking.uuid,
        route_uuid=get_booking.route_uuid,
        user_uuid=get_booking.user_uuid,
        status=get_booking.status,

        selected_seats=[
            GetSelectedSeatSchema(
                uuid=seat.uuid,
                seat_uuid=seat.seat_uuid,
            )
            for seat in all_seats
        ],

        lugggages=(
            GetLuggagesSchema(
                uuid=luggage.uuid,
                number_of_luggages=luggage.number_of_luggages,
                weight_of_luggages=luggage.weight_of_luggages,
                price=luggage.price,
            )
            if luggage
            else None
        ),
    )     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        