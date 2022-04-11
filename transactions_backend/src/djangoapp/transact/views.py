from rest_framework.decorators import api_view

from utils import api_utils
@api_view(["GET"])
def summary(request):
    return api_utils.response_success()

