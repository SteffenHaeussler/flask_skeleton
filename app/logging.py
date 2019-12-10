from datetime import datetime as dt
from typing import Dict

import json
import logging.config

from pythonjsonlogger.jsonlogger import JsonFormatter

from flask import current_app
from werkzeug.local import LocalProxy


logger = LocalProxy(lambda: current_app.logger)


def setup_logging(config: Dict) -> None:
    """
    Set set level of the Flask logger to ERROR,
    in that case only errors are logged. Then setup the service logging schema.
    :param config: log settings
    :return:
    """
    def _disable_logger(name):
        flask_log = logging.getLogger(name)
        flask_log.setLevel(logging.ERROR)
    _disable_logger("werkzeug")
    _disable_logger("alembic.runtime.migration")
    _disable_logger("alembic.autogenerate.compare")
    _disable_logger("urllib3")
    _disable_logger("requests")
    logging.config.dictConfig(config)


def get_logger_settings(debug=0):
    log_level = logging.DEBUG if debug else logging.INFO

    settings = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {"global": {"()": "app.logging.GlobalFilter"}},
        "formatters": {
            "json": {
                "format": "[%(name)s %(ts)s %(version)s %(level)s %(message)s %(category)s]",
                "class": "app.logging.CustomJsonFormatter",
            }
        },
        "handlers": {
            "json": {
                "class": "logging.StreamHandler",
                "formatter": "json",
                "filters": ["global"],
            }
        },
        "loggers": {"": {"handlers": ["json"], "level": log_level}},
    }
    return settings


def version_filter() -> str:  # pragma: no cover
    return "0.1.0"


def timestamp_filter() -> str:  # pragma: no cover
    now = dt.utcnow()
    DT_FMT = "%Y-%m-%dT%H:%M:%S%Z"
    return now.strftime(DT_FMT)


class GlobalFilter(logging.Filter):  # pragma: no cover
    def filter(self, record):
        record.version = version_filter()
        record.ts = timestamp_filter()
        record.level = record.levelname
        record.category = record.name
        return True


class CustomJsonFormatter(JsonFormatter):  # pragma: no cover
    def process_log_record(self, log_record):
        if "exc_info" in log_record:
            log_record["stack"] = log_record.pop("exc_info")
        return log_record
