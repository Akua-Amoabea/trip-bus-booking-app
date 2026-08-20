from pydantic import BaseModel
from uuid import UUID

class SelectedSeatSchema(BaseModel):
    seat_uuid: UUID
    route_uuid: UUID
    booking_uuid:UUID
    

class GetSelectedSeatSchema(BaseModel):
    uuid: UUID
    seat_uuid:UUID
    
    
    
    
        