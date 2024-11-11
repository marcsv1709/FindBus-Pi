from flask_login import current_user
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_user_profile(self):
        return self.user_repository.get_user_by_id(current_user.id)

    def update_user_profile(self, username, email):
        user = self.user_repository.get_user_by_id(current_user.id)
        if user:
            user.username = username
            user.email = email
            return self.user_repository.save_user(user)
        return None

    def update_user_password(self, password):
        user = self.user_repository.get_user_by_id(current_user.id)
        if user:
            user.set_password(password)
            return self.user_repository.save_user(user)

    def delete_user_profile(self):
        return self.user_repository.delete_user_by_id(current_user.id)
