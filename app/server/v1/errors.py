from flask import jsonify

from . import logger
from . import v1


class APIError(Exception):

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['code'] = self.status_code
        rv['message'] = self.message
        return rv


@v1.app_errorhandler(APIError)
def bad_request(error):
    logger.error(error.to_dict())
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@v1.app_errorhandler(400)
def bad_request(error):
    response = {'code': 400, 'error': 'bad request', 'message': repr(error)}
    logger.error(response)
    response = jsonify(response)
    response.status_code = 400
    return response


@v1.app_errorhandler(500)
def internal_server_error(error):
    response = {'code': 500, 'error': 'internal server error',
                'message': repr(error)}
    logger.error(response)
    response = jsonify(response)
    response.status_code = 500
    return response


@v1.app_errorhandler(403)
def forbidden(error):
    response = {'code': 403, 'error': 'forbidden', 'message': repr(error)}
    logger.error(response)
    response = jsonify(response)
    response.status_code = 403
    return response
