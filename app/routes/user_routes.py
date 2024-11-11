from flask import Blueprint, request
from flask_login import login_required
from app.controller.user_controller import UserController

user_routes = Blueprint("user_routes", __name__)
user_controller = UserController()


@user_routes.route("/user", methods=["GET"])
@login_required
def get_profile():
    return user_controller.get_profile()


@user_routes.route("/user/edit-profile", methods=["PUT"])
@login_required
def edit_profile():
    data = request.json
    return user_controller.edit_profile(data)


@user_routes.route("/user/new-password", methods=["PUT"])
@login_required
def new_password():
    data = request.json
    return user_controller.new_password(data)


@user_routes.route("/user/delete", methods=["DELETE"])
@login_required
def delete_profile():
    return user_controller.delete_profile()
