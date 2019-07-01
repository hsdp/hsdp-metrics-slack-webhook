import os
from flask import Flask, jsonify
from flask.logging import default_handler
from config import config


def create_application():
    app = Flask(__name__)
    app.config.from_object(config)
    app.logger.removeHandler(default_handler)

    from controllers.webhook_proxy import webhook_proxy
    app.register_blueprint(webhook_proxy)

    simple_errors = (400, 401, 404, 403)

    def simple_error(e):
        return jsonify({'error': e.code, 'message': e.description}), e.code

    for error in simple_errors:
        app.errorhandler(error)(simple_error)

    return app
