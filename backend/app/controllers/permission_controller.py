from flask import (
    render_template,
    request,
    redirect,
    flash,
    url_for
)

from app.services.permission_service import PermissionService


class PermissionController:

    @staticmethod
    def index():

        permissions = PermissionService.get_all()

        return render_template(
            "permission/list.html",
            permissions=permissions
        )

    @staticmethod
    def create():

        if request.method == "GET":

            return render_template(
                "permission/add.html"
            )

        code = request.form.get("code")

        name = request.form.get("name")

        module = request.form.get("module")

        description = request.form.get("description")

        PermissionService.create(
            code,
            name,
            module,
            description
        )

        flash(
            "Permission added successfully.",
            "success"
        )

        return redirect(
            url_for("permission.index")
        )

    @staticmethod
    def edit(permission_id):

        if request.method == "GET":

            permission = PermissionService.find_by_id(
                permission_id
            )

            return render_template(
                "permission/edit.html",
                permission=permission
            )

        code = request.form.get("code")

        name = request.form.get("name")

        module = request.form.get("module")

        description = request.form.get("description")

        PermissionService.update(
            permission_id,
            code,
            name,
            module,
            description
        )

        flash(
            "Permission updated successfully.",
            "success"
        )

        return redirect(
            url_for("permission.index")
        )

    @staticmethod
    def delete(permission_id):

        PermissionService.delete(permission_id)

        flash(
            "Permission deleted successfully.",
            "success"
        )

        return redirect(
            url_for("permission.index")
        )