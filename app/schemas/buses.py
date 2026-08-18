
from pydantic import BaseModel
from uuid import UUID

class CreateBusSchema(BaseModel):
    bus_number: str
    capacity: int
    
    
class GetBusSchema(BaseModel):
    uuid: UUID  
    bus_number:str
    capacity: int
    
     
    
    
        