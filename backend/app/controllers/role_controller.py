from flask import (render_template, request, redirect, flash, url_for)

from app.services.role_service import RoleService

class RoleController:

    @staticmethod
    def index():

        roles = RoleService.get_all()

        return render_template(
            "role/list.html",
            roles = roles
        )

    @staticmethod
    def create():

        if request.method == "GET":

            return render_template(
                "role/add.html"
            )

        name = request.form.get("name")

        description = request.form.get("description")

        RoleService.create(
            name,
            description
        )

        flash(
            "Successfully added a role.",
            "success"
        )

        return redirect(
            url_for("role.index")
        )

    @staticmethod
    def edit(role_id):

        if request.method == "GET":

            role = RoleService.find_by_id(role_id)

            return render_template(
                "role/edit.html",
                role = role
            )

        name = request.form.get("name")

        description = request.form.get("description")

        RoleService.update(
            role_id,
            name,
            description
        )

        flash(
            "Successfully updated a role.",
            "success"
        )

        return redirect(
            url_for("role.index")
        )

    @staticmethod
    def delete(role_id):

        RoleService.delete(role_id)

        flash(
            "Successfully deleted a role.",
            "success"
        )

        return redirect(
            url_for("role.index")
        )

