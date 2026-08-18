from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel


class CreateBusSchema(BaseModel):
    leaving_time: time
    destination_time: time
    with_ac: bool
    location: str
    destination: str
    price: Decimal
    leaving_date: date