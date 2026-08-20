from pydantic import BaseModel
from uuid import UUID

class AddLuggagesSchema(BaseModel):
   number_of_luggages: int
   weight_of_luggages:float
  
    

class GetLuggagesSchema(BaseModel):
   uuid: UUID 
   number_of_luggages: int
   weight_of_luggages:float
        