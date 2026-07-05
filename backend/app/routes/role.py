from flask import Blueprint

from app.controllers.role_controller import RoleController
from app.middlewares.login_required import login_required

role_bp = Blueprint(
    "role",
    __name__,
    url_prefix="/roles"
)

role_bp.add_url_rule(
    "/",
    view_func=login_required(RoleController.index),
    methods=["GET"]
)

role_bp.add_url_rule(
    "/add",
    view_func=login_required(RoleController.create),
    methods=["GET", "POST"]
)

role_bp.add_url_rule(
    "edit/<int:role_id>",
    view_func=login_required(RoleController.edit),
    methods=["GET", "POST"]
)

role_bp.add_url_rule(
    "delete/<int:role_id>",
    view_func=login_required(RoleController.delete),
    methods=["GET"]
)