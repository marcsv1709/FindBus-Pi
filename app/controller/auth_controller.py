from flask import jsonify, request
from flask_login import login_user, logout_user
from app.model.user_model import User, db

class AuthController:

    @staticmethod
    def register():
        data = request.json
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.query.filter_by(username=username).first():
            return jsonify({"error": "Username already exists"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already exists"}), 400

        new_user = User(username=username)
        new_user.set_password(password)
        new_user.email = email
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201

    @staticmethod
    def login():
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            login_user(user)
            return jsonify({"message": "Login successful"}), 200
        return jsonify({"error": "Invalid credentials"}), 401

    @staticmethod
    def logout():
        logout_user()
        return jsonify({"message": "Logout successful"}), 200
