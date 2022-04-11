from dataclasses import dataclass


class Command:
    pass


@dataclass
class CreateTransaction(Command):
    company_id: str
    price: int
    status: str
    approve_status: str