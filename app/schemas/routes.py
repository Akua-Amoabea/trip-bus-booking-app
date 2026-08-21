from datetime import date, time, datetime
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID

from app.schemas.locations import GetLocationSchema


class CreateRouteSchema(BaseModel):
    leaving_time: time
    destination_time: time
    location_uuid: UUID
    destination_uuid: UUID
    price: float
    leaving_date: date
    bus_uuid:UUID
    
    

class GetRouteSchema(BaseModel):
    uuid: UUID
    leaving_time: time
    destination_time: time
    location: GetLocationSchema
    destination: GetLocationSchema
    price: float
    leaving_date: date  
    created_time:datetime 
    bus_uuid:UUID
    
    
 
class FilterRouteSchema(BaseModel):
    uuid: Optional[UUID] = None 
    leaving_time: Optional[time]= None
    destination_time: Optional[time]= None
    location_uuid: Optional[UUID] = None
    destination_uuid: Optional[UUID] = None
    price: Optional[float]=None
    leaving_date: Optional[date] = None
    created_time:Optional[datetime] = None 
    bus_uuid:Optional[UUID] = None
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=10, ge=1, le=30)



class GetAllRouteSchema(BaseModel):
    routes: list[GetRouteSchema]
    page: int
    limit: int
    total_count: int
    total_pages: int
    
         