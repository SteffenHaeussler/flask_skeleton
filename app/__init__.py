#! ../env/bin/python
# -*- coding: utf-8 -*-


from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from app.config import config
from app.logging import setup_logging, get_logger_settings


def create_app(config_name, logging_flag=True):
    """
    Create the Flask app.

    Params

    config_name: string
        sets specific config flags

    logging_flag: boolean
        enables/disables logging

    Returns:

    app: object
        flask app
    -------
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    log_setting = get_logger_settings(app.config["DEBUG"])
    setup_logging(log_setting)

    from .server.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .server.v1 import v1 as v1_blueprint
    app.register_blueprint(v1_blueprint, url_prefix="/v1")

    swaggerui_blueprint = get_swaggerui_blueprint(
        app.config["SWAGGER_UI_URL"],
        app.config["SWAGGER_JSON_URL"],
        config={"app_name": "Test application"})

    app.register_blueprint(swaggerui_blueprint,
                           url_prefix=app.config["SWAGGER_UI_URL"])

    app.logger.info("API running in %s mode", config_name)

    return app


