from time import time

from flask import current_app as app
from flask import request, jsonify

from app.server.v1.errors import *


@v1.before_request
def before_request():
    logger.debug('Incoming request!')
    return None


@v1.after_request
def after_request(response):
    logger.debug('Closing request!')
    return response


@v1.route("/health", methods=["GET", "POST"])
def health():
    return jsonify({"version": app.config['VERSION'], "timestamp": time()})
