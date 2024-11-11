from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "findbus.db"


def init_app(app: Flask):

    app.config["SECRET_KEY"] = "asdasdsadasdsadasdasdsd"
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"sqlite:///{path.join(app.root_path, DB_NAME)}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()