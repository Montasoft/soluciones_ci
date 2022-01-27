from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true
#from flask_migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    # load the config file specified by the APP enviroment varibale
    app.config.from_object(settings_module)
    # load the configuration form the instance folder
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)

    login_manager.init_app(app)
    login_manager.login_view = "login"


    db.init_app(app)
    
    # Registro de los Blueprints
    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)
    
    return app

