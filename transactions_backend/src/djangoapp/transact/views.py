import logging

from rest_framework.decorators import api_view
from rest_framework import status

from transactions.service_layer import unit_of_work
from transactions.domain.model import NotFoundException
from utils import api_utils
from transactions.service_layer import views


logger = logging.getLogger(__name__)
@api_view(["GET"])
def summary(request):
    logger.info("call get summary")
    uow = unit_of_work.DjangoUnitOfWork()
    transaction = views.get_summary(unit_of_work=uow)
    return api_utils.response_success(data=transaction)


@api_view(["GET"])
def company_detail(request, company_id):
    logger.error("call get company_detail")
    uow = unit_of_work.DjangoUnitOfWork()
    try:
        company_info = views.get_company_summary(unit_of_work=uow, company_id=company_id)
    except NotFoundException as e:
        return api_utils.response_error(
            error_code=api_utils.ErrorCode.NOT_FOUND,
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        logger.exception("Error unknown.")
        raise e
        

    return api_utils.response_success(data=company_info)

