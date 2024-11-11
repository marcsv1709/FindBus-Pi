from flask import Flask
from app.model.user_model import User
from app.routes.user_routes import user_routes
from app.routes.auth_routes import auth_routes
from app.database.db import init_app, db
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)

    init_app(app)
    
    app.register_blueprint(user_routes, url_prefix="/")
    app.register_blueprint(auth_routes, url_prefix="/")


    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth_routes.login"


    # Carregar usuário para o Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Configuração da página de login para o Flask-Login
    login_manager.login_view = "auth_routes.login"
    login_manager.login_message_category = "info"

    # Criar o banco de dados, se necessário
    with app.app_context():
        db.create_all()

    print(app.url_map)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
