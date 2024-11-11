from flask import Blueprint
from app.controller.auth_controller import AuthController

auth_routes = Blueprint("auth_routes", __name__)

auth_routes.route("/register", methods=["POST"])(AuthController.register)
auth_routes.route("/login", methods=["POST"])(AuthController.login)
auth_routes.route("/logout", methods=["POST"])(AuthController.logout)
