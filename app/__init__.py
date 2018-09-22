from flask import Flask
from instance.config import DevelopmentConfig


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    return app
