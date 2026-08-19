from pydantic import BaseModel
from uuid import UUID

class AddSeatsSchema(BaseModel):
   seat_number:str
   is_available:bool
   route_uuid: UUID
   bus_uuid: UUID
   
   
class GetSeatsSchema(BaseModel):
    uuid:UUID
    seat_number:str
    is_available:bool
    route_uuid: UUID
    bus_uuid: UUID
       
   