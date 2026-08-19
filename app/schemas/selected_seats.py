from pydantic import BaseModel
from uuid import UUID

class SelectedSeat(BaseModel):
    seat_uuid: UUID
    route_uuid: UUID
    

class GetSelectedSeat(BaseModel):
    uuid: UUID
    seat_uuid:UUID
    route_uuid:UUID
    
    
        