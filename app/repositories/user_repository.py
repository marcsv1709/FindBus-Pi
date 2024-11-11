from app.model.user_model import User
from app.database.db import db

class UserRepository:
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def save_user(self, user):
        try:
            db.session.commit()
            return user
        except Exception as e:
            print(f"Error saving user: {e}")
            return None

    def delete_user_by_id(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
                return True
            except Exception as e:
                print(f"Error deleting user: {e}")
                return False
        return False
