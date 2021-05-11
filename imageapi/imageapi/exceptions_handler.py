import json

from rest_framework.views import exception_handler


def json_exception_handler(exc, context):
    response = exception_handler(exc, context)
    response.content_type = 'application/json'
    response.data = json.dumps(response.data).encode('utf-8')
    return response
