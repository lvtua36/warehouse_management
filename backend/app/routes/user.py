from flask import Blueprint

from app.controllers.user_controller import UserController
from app.middlewares.login_required import login_required

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/users"
)

user_bp.add_url_rule(
    "/",
    view_func=login_required(UserController.index),
    methods=["GET"]
)

user_bp.add_url_rule(
    "/add",
    view_func=login_required(UserController.create),
    methods=["GET", "POST"]
)

user_bp.add_url_rule(
    "/edit/<int:user_id>",
    view_func=login_required(UserController.edit),
    methods=["GET", "POST"]
)

user_bp.add_url_rule(
    "/delete/<int:user_id>",
    view_func=login_required(UserController.delete),
    methods=["GET"]
)