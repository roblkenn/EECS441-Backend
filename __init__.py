import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
    SECRET_KEY='dev',
    )

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    import auth
    app.register_blueprint(auth.bp)

    return app
