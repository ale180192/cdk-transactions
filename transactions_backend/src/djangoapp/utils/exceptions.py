from transactions_backend.src.djangoapp.utils import error_code
from utils.error_code import ErrorCode

class APIExceptions(Exception):

    def __init__(
        self,
        error_code: ErrorCode,
        status_code: int = 500,
        error_detail: str = None,
        errors: list = None
    ):
        self. error_code = error_code
        self.status_code = status_code
        self.error_detail = error_detail if error_detail else error_code.value
        self.errors = errors
