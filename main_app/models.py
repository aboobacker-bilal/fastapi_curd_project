from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import datetime


class Item(BaseModel):
    name: str
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: int = int(datetime.timestamp(datetime.now()))


class ClockInRecord(BaseModel):
    email: EmailStr
    location: str
    insert_date: Optional[datetime] = None
