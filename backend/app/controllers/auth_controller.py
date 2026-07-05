from flask import (
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

from app.services.auth_service import AuthService

class AuthController:

    @staticmethod
    def login():

        if request.method == "GET":

            return render_template(
                "auth/login.html"
            )

        username = request.form.get("username")

        password = request.form.get("password")

        user = AuthService.login(
            username,
            password
        )

        if user is None:

            flash(
                "Incorrect account or password.",
                "danger"
            )

            return redirect(url_for("auth.login"))

        session["user_id"] = user["id"]

        session["username"] = user["username"]

        session["role_id"] = user["role_id"]

        return redirect("/dashboard")

    @staticmethod
    def logout():

        session.clear()

        return redirect("/login")