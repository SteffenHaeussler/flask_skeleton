from flask import jsonify

from . import main
from . import logger


@main.app_errorhandler(400)
def bad_request(error):
    response = {'code': 400, 'error': 'bad request', 'message': repr(error)}
    logger.error(response)
    response = jsonify(response)
    response.status_code = 400
    return response


@main.app_errorhandler(500)
def internal_server_error(error):
    response = {'code': 500, 'error': 'internal server error', 'message': repr(error)}
    logger.error(response)
    response = jsonify(response)
    response.status_code = 500
    return response


@main.app_errorhandler(403)
def forbidden(error):
    response = {'code': 403, 'error': 'forbidden', 'message': repr(error)}
    logger.error(response)
    response = jsonify(response)
    response.status_code = 403
    return response
