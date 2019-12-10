from time import time

from flask import current_app as app
from flask import request, jsonify

from app.server.main.errors import *



@main.before_request
def before_request():
    logger.debug('Incoming request!')
    return None


@main.after_request
def after_request(response):
    logger.debug('Closing request!')
    return response


@main.route('/health', methods=['GET', 'POST'])
def health():
    logger.debug(f'Methode: {request.method} on {request.path}')
    return jsonify({
        'version': app.config['VERSION'],
        'timestamp': time()
    })


@main.route('/docs/swagger.json', methods=['GET'])
def get_openapi():
    logger.debug(f'Methode: {request.method} on {request.path}')
    return jsonify(app.config['SWAGGER'])
