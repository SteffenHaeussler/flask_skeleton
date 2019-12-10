import os
from os.path import abspath, dirname, join
from yaml import Loader, load


class BaseConfig(object):
    """Base configuration."""

    VERSION = "0.1.0"

    CONFIG_NAME = ""
    DEBUG = True

    # reduce size of api response
    JSONIFY_PRETTYPRINT_REGULAR = False

    BASEDIR = abspath(dirname(__file__))
    # credentials if neeet
    GITLAB_USERNAME = os.environ.get("GITLAB_USERNAME")
    GITLAB_PASSWORD = os.environ.get("GITLAB_PASSWORD")

    # Swagger setup
    SWAGGER = load(open(join(BASEDIR, "swagger.yml")), Loader=Loader)
    SWAGGER_UI_URL = "/docs"  # URL for exposing Swagger UI
    SWAGGER_JSON_URL = "../docs/swagger.json" # Where to serve swagger.json from


    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    DEBUG = False

    @classmethod
    def init_app(cls, app):
        BaseConfig.init_app(app)


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "develop"
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        BaseConfig.init_app(app)


class StagingConfig(BaseConfig):
    CONFIG_NAME = "staging"
    DEBUG = False

    @classmethod
    def init_app(cls, app):
        BaseConfig.init_app(app)


class TestingConfig(BaseConfig):
    CONFIG_NAME = "testing"
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        BaseConfig.init_app(app)


class SandboxConfig(BaseConfig):
    CONFIG_NAME = "sandbox"
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        BaseConfig.init_app(app)


config = {
    "prod": ProductionConfig,
    "develop": DevelopmentConfig,
    "staging": StagingConfig,
    "testing": TestingConfig,
    "sandbox": SandboxConfig
}

