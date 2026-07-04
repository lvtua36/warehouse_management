from flask import Flask
from app.config import Config
from app.extensions import bcrypt
from app.routes.auth import auth_bp

def create_app():

    app = Flask(
        __name__,
        template_folder="../../frontend/templates",
        static_folder="../../frontend/static"
    )

    app.config.from_object(Config)

    bcrypt.init_app(app)

    app.register_blueprint(auth_bp)

    return app