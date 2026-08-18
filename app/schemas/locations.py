from pydantic import BaseModel
from uuid import UUID

class CreateLocationSchema(BaseModel):
    name: str
    
   
class GetLocationSchema(BaseModel):
    uuid:UUID
    name:str
    
    
       
    
    
    