from flask import jsonify
from flask_login import current_user
from app.service.user_service import UserService


class UserController:
    def __init__(self):
        self.user_service = UserService()

    def get_profile(self):
        return jsonify(current_user.to_dict()), 200

    def edit_profile(self, data):
        username = data.get("username")
        email = data.get("email")

        if not email or len(email) < 4:
            return jsonify({"error": "Invalid email."}), 400
        if not username or len(username) < 2:
            return jsonify({"error": "User name too short."}), 400

        updated_user = self.user_service.update_user_profile(username, email)
        if updated_user:
            return jsonify({"message": "Profile updated successfully."}), 200
        return jsonify({"error": "Failed to update profile."}), 500

    def new_password(self, data):
        password = data.get("password")
        if not password or len(password) < 6:
            return jsonify({"error": "Password too short."}), 400

        updated_user_password = self.user_service.update_user_password(password)
        if updated_user_password:
            return jsonify({"message": "Password updated successfully."}), 200
        return jsonify({"error": "Failed to update password."}), 500

    def delete_profile(self):
        success = self.user_service.delete_user_profile()
        if success:
            return jsonify({"message": "Account deleted successfully."}), 200
        return jsonify({"error": "Failed to delete account."}), 500
