from operator import rshift
from .unit_of_work import DjangoUnitOfWork

def get_summary(unit_of_work: DjangoUnitOfWork) -> dict:
    with unit_of_work as uow:
        summary = uow.transactions.get_summary()

    return summary

def get_company_summary(
    unit_of_work: DjangoUnitOfWork,
    company_id: str
) -> dict:
    with unit_of_work as uow:
        company_info = uow.transactions.get_company_summary(id=company_id)

    return company_info