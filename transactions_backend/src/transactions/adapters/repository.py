
import abc

from django.db.models import Sum, Q, Count
from django.db.models.functions import TruncDate

from transactions.domain import model
from transact.models import (
    Transaction as TransactionORM,
    Company as CompanyOrm
)

class AbstractRepository(abc.ABC):
    
    @abc.abstractmethod
    def get_summary(self):
        raise NotImplementedError

class DjangoRepository(AbstractRepository):
    
    def _get_company_more_sales(self) -> tuple[str, float]:
        query = TransactionORM.objects \
            .values("company__name", "status") \
            .order_by("company__name") \
            .annotate(total=Sum("price", filter=Q(charged=True))) \
            .order_by("-total").first()
            
        if not query:
            return None

        return (
            query["company__name"],
            query["total"]
        )

    def _get_company_less_sales(self) -> tuple[str, float]:
        from django.db.models import Subquery
        query = TransactionORM.objects \
            .values("company__name") \
            .order_by("company__name") \
            .annotate(total=Sum("price", filter=Q(charged=True))) \
            .order_by("total")

        companies = []
        for company in query:
            if company["total"] is not None:
                companies.append(company)

        if not companies:
            return None

        
        return (
            companies[0]["company__name"],
            companies[0]["total"]
        )


    def _get_total_transactions_amount(self):
        amount = TransactionORM.objects \
            .aggregate(
                not_charged_total=Sum("price", filter=Q(charged=False)),
                charged_total=Sum("price", filter=Q(charged=True))
            )

        return amount["charged_total"], amount["not_charged_total"]


    def _get_total_company_more_not_charged(self):
        query = TransactionORM.objects \
            .values("company__name", "status") \
            .order_by("company__name") \
            .annotate(total=Sum("price", filter=Q(charged=False))) \
            .order_by("-total").first()
            
        if not query:
            return None

        return (
            query["company__name"],
            query["total"]
        )


    def get_summary(self):
        company_less, total_less = self._get_company_less_sales()
        company_more, total_more, = self._get_company_more_sales()
        charged_total, not_charged_total = self._get_total_transactions_amount()
        company, not_charged_company = self._get_total_company_more_not_charged()

        return {
            "company_more_sales": {
                "name": company_more,
                "total": total_more
            },
            "company_less_sales": {
                "name": company_less,
                "total" : total_less
            },
            "transactions_total": {
                "charged": charged_total,
                "not_charged": not_charged_total
            },
            "company_more_sales_not_charged": {
                "company": company,
                "total": not_charged_company
            }
        }
    
    def get_company_summary(self, id: str) -> dict:
        company = CompanyOrm.objects.filter(id=id).first()
        if not company:
            raise model.NotFoundException()

        charged = TransactionORM.objects \
            .aggregate(
                charged=Sum(
                    "price",
                    filter=Q(charged=True) & Q(company=company) 
                ),
            )

        not_charged = TransactionORM.objects \
            .aggregate(
                charged=Sum(
                    "price",
                    filter=Q(charged=True) & Q(company=company) 
                ),
            )

        results = TransactionORM.objects \
            .values("company", date=TruncDate("created_at")) \
            .annotate(total=Count(TruncDate("created_at"), filter=Q(company=company))) \
            .order_by("-total")

        date = None
        count_transactions = None
        if results:
            date = results[0]["date"]
            count_transactions = results[0]["total"]
        

        return {
            "name": company.name,
            "transactions": {
                "charged": charged,
                "not_charged": not_charged
            },
            "day_more_transactions": {
                "date": date,
                "total": count_transactions,
            }
        }

