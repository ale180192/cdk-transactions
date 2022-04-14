from datetime import datetime
from enum import Enum
from pydantic import UUID4

from pydantic import BaseModel

class NotFoundException(Exception):
    pass

class Company(BaseModel):
    id: UUID4
    name: str
    
    class Config:
        orm_mode = True

class Transaction(BaseModel):
    id: UUID4
    company: Company
    price: int
    created_at: datetime
    status: str
    approved: bool
    class Config:
        orm_mode = True
    class StatusEnum(Enum):
        CLOSED = "CLOSED"
        REVERSED = "REVERSED"
        PENDING = "PENDING"

    def __init__(self,
        id: str,
        company: Company,
        price: int,
        created_at: datetime,
        status: StatusEnum,
        approved: bool,
    ):
        self.id = id
        self.company = company
        self.price = price
        self.created_at = created_at
        self.status = status
        self.approved = approved
        self.charged = True if (approved and status == self.StatusEnum.CLOSED.value) \
            else False
        
