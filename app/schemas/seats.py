from pydantic import BaseModel
from uuid import UUID

class AddSeatsSchema(BaseModel):
   seat_number:str
   bus_uuid: UUID
   
   
class GetSeatsSchema(BaseModel):
    uuid:UUID
    seat_number:str
    bus_uuid: UUID
       
   