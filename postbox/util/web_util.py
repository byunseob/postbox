from flask import request
from werkzeug.exceptions import BadRequest


def request_param(name, default=None, type=None, required: bool = False, error_message: str = None):
    value = request.values.get(name, default=default, type=type)

    if required and not value:
        raise BadRequest(error_message if error_message else 'Required is {}'.format(name))

    return value
