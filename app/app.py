from flask import Flask, jsonify, request, redirect
from core.extensions import cors, db, login_manager, mail, migrate, toolbar


def create_app(config_name='dev'):
    config_map = {
        'dev': 'core.config.Development',
        'develop': 'core.config.Development',
        'test': 'core.config.Testing',
        'testing': 'core.config.Testing',
        'prod': 'core.config.Production',
        'production': 'core.config.Production',
    }

    app = Flask(__name__)
    app.config.from_object(config_map[config_name])

    cors.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    toolbar.init_app(app)
    mail.init_app(app)

    def _force_https():
        """ Redirect any non-https requests to https.
        """
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            r = redirect(url, code=code)
            return r

    if not app.config['DEBUG']:
        app.before_request(_force_https)

    # Need to load models before initializing Migration extension
    from core.models import Counter  # noqa
    migrate.init_app(app, db)

    register_blueprints(app)
    add_session_rollback(app)
    add_error_handlers(app)

    return app


def register_blueprints(app):
    import core.controllers as core_controllers

    app.register_blueprint(core_controllers.routes)


def add_session_rollback(app):
    @app.teardown_request
    def teardown_request(exception):
        if exception:
            db.session.rollback()
        db.session.remove()


class APIError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def add_error_handlers(app):
    @app.errorhandler(APIError)
    def handle_value_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code

        return response
