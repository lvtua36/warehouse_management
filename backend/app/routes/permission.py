from flask import Blueprint

from app.controllers.permission_controller import PermissionController
from app.middlewares.login_required import login_required

permission_bp = Blueprint(
    "permission",
    __name__,
    url_prefix="/permissions"
)

permission_bp.add_url_rule(
    "/",
    view_func=login_required(PermissionController.index),
    methods=["GET"]
)

permission_bp.add_url_rule(
    "/add",
    view_func=login_required(PermissionController.create),
    methods=["GET", "POST"]
)

permission_bp.add_url_rule(
    "/edit/<int:permission_id>",
    view_func=login_required(PermissionController.edit),
    methods=["GET", "POST"]
)

permission_bp.add_url_rule(
    "/delete/<int:permission_id>",
    view_func=login_required(PermissionController.delete),
    methods=["GET"]
)