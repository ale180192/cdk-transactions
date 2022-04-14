from rest_framework.views import Response
from rest_framework import status

from .error_code import ErrorCode

def response_error(error_code: ErrorCode, status: int, error_detail: str = None, errors: dict = {}):
    """
    This function is a wrapper to homology the body of the error responses
    :param error_code: an error enum of the ErrorCode class
    :param status: The appropriate http code for the answer
    :param error_detail: This parameter indicates some custom detail to be used instead 
    of the default by the ErrorCode enumeration class.
    :param errors: this field indicates a list of errors, useful in the case of validating forms
    :return Response: Returns a Response object with the body correctly formatted
    """
    if not error_detail:
        error_detail = error_code.value
    error = {
        "ok": False,
        "error": {
            "status": status,
            "error_code": error_code.name,
            "detail": error_detail,
            "errors": errors
        }
    }
    return Response(data=error, status=status)


def response_success(data=None, status=status.HTTP_200_OK):
    """
    This function homologates the response to a body with 2 fields -> ok and data
    :param data: this value will be appended directly to the data field
    :status: The appropriate http code for the answer, by default it has a status 200
    """
    data = {
        "ok": True,
        "data": data
    }
    return Response(data=data, status=status)
