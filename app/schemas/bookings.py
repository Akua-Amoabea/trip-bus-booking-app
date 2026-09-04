from pydantic import BaseModel
from uuid import UUID
from typing import Optional

from app.schemas.luggages import AddLuggagesSchema, GetLuggagesSchema
from app.schemas.selected_seats import GetSelectedSeatSchema

class AddBookingsSchema(BaseModel):
   route_uuid: UUID
   user_uuid: UUID
   status: float
   

class GetBookingsSchema(BaseModel):
    uuid:UUID
    route_uuid: UUID
    user_uuid: UUID
    status:str   
    selected_seats: list[GetSelectedSeatSchema]
    lugggages: Optional[GetLuggagesSchema] = None
    


class CreateBookingsSchema(BaseModel):
    user_uuid: UUID
    route_uuid: UUID
    selected_seats: list[UUID]
    luggages: Optional[AddLuggagesSchema] = None


class UpdateBookingsSchema(BaseModel):
    status: str
    
   
        