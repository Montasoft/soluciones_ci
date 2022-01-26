from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Jorge:Meneses1@localhost:5432/SCI_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    login_manager.init_app(app)
    login_manager.login_view = "admin.login"
    db.init_app(app)
    db.create_all

    # Registro de los Blueprints
    from .admin import admin_bp
    app.register_blueprint(admin_bp)
    from .public import public_bp
    app.register_blueprint(public_bp)
    return app