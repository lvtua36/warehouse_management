from flask import render_template

from app.services.user_service import UserService


class UserController:

    @staticmethod
    def index():

        users = UserService.get_all()

        return render_template(
            "user/list.html",
            users=users
        )

    @staticmethod
    def create():
        return render_template("user/add.html")

    @staticmethod
    def edit(user_id):
        return render_template("user/edit.html")

    @staticmethod
    def delete(user_id):
        return "Delete User"