import os

from flask import Flask

from app.config import Config

from app.extensions import bcrypt

from app.routes.auth import auth_bp
from app.routes.dashboard import dashboard_bp
from app.routes.role import role_bp
from app.routes.permission import permission_bp
from app.routes.user import user_bp

def create_app():

    base_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )

    template_dir = os.path.join(
        base_dir,
        "frontend",
        "templates"
    )

    static_dir = os.path.join(
        base_dir,
        "frontend",
        "static"
    )

    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=static_dir
    )

    app.config.from_object(Config)

    bcrypt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(permission_bp)
    app.register_blueprint(user_bp)

    return app