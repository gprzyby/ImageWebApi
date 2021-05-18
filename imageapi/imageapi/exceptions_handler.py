from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
import logging


def create_default_error_response(exc: Exception) -> Response:
    logging.error('Error in fetching data: {}', exc)
    return Response(data={'detail': str(exc)},
                    status=HTTP_500_INTERNAL_SERVER_ERROR,
                    content_type='application/json')


def json_exception_handler(exc, context):
    response = exception_handler(exc, context) or create_default_error_response(exc)
    response.content_type = 'application/json'
    return response
