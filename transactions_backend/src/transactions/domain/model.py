from datetime import datetime
from enum import Enum


class Company:
    
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def some_business_rule(self):
        pass

class Transaction:

    class StatusEnum(Enum):
        CLOSED = "CLOSED"
        REVERSED = "REVERSED"
        PENDING = "PENDING"

    def __init__(self,
        id: str,
        company_id: str,
        price: int,
        created_at: datetime,
        status: StatusEnum,
        approved: bool,
    ):
        self.id = id
        self.company_id = company_id
        self.price = price
        self.created_at = created_at
        self.status = status
        self.approved = approved
        self.charged = True if (approved and status == self.StatusEnum.CLOSED.value) \
            else False
        
