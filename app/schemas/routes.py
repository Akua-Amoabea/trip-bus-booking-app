from datetime import date, time, datetime
from pydantic import BaseModel
from uuid import UUID


class CreateRouteSchema(BaseModel):
    leaving_time: time
    destination_time: time
    with_ac: bool
    location_uuid: UUID
    destination_uuid: UUID
    price: float
    leaving_date: date
    
    

class GetRouteSchema(BaseModel):
    uuid: UUID
    leaving_time: time
    destination_time: time
    with_ac: bool
    location_uuid: UUID
    destination_uuid: UUID
    price: float
    leaving_date: date  
    created_time:datetime 