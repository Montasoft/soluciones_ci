from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true
from flask_wtf.csrf import CSRFProtect
import os
from flask_migrate import Migrate
from flask_mail import Mail
from logging.handlers import SMTPHandler


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()   # Instanciamos un objeto de tipo Mail

settings_module= os.getenv('APP_SETTINGS_MODULE')

#def create_app(settings_module= 'config.DevelopmentConfig'):
def create_app():
    #app = Flask(__name__, instance_relative_config=True)
#app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)
    
   # sqlalchemy = SQLAlchemy()
    #sqlalchemy.init_app(app)

    # load the config file specified by the APP enviroment varibale
    app.config.from_object(settings_module)

    
#app.secret_key = os.urandom(24) #24 bits
#csrf = CSRFProtect(app)

    #   app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/sci_db'
    #  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    #migrate = Migrate(app,db)

#db.init_app(app)
#migrate.init_app(app,db)
    #  mail.init_app(app) # iniciamos el objeto mail.

    #db.create_all()


    
    # load the configuration form the instance folder
    # comento 3
    #if app.config.get('TESTING', False):
    #    app.config.from_pyfile('config-testing.py', silent=True)
    #else:
#app.config.from_pyfile('config.py', silent=True)
    app.config.from_pyfile('config.local.py', silent=True)
    login_manager.init_app(app)
    login_manager.login_view = "login"

   # db.init_app(app)
    
    # Registro de los Blueprints
    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)
    
    mail_setting = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
#"MAIL_USERNAME": os.environ['MAIL_USERNAME'],
        "MAIL_USERNAME": 'papeleria5613837@gmail.com',
#"MAIL_PASSWORD": os.environ['MAIL_PASSWORD'],
        "MAIL_PASSWORD": 'meneses1',
        "DONT_REPLY_FROM_EMAIL": '(jorge, papeleria5613837@gmail.com)',
        "ADMINS": "('papeleria5613837@gmail.com', )"
    }

    app.config.update(mail_setting)
    mail = Mail(app)
    

    return app



'''
mail_handler = SMTPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                                   app.config['DONT_REPLY_FROM_EMAIL'],
                                   app.config['ADMINS'],
                                   '[Error][{}] La aplicación falló'.format(app.config['APP_ENV']),
                                   (app.config['MAIL_USERNAME'],
                                    app.config['MAIL_PASSWORD']),
                                   ())
        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(mail_handler_formatter())
        handlers.append(mail_handler)

    for l in loggers:
        for handler in handlers:
            l.addHandler(handler)
        l.propagate = False
        l.setLevel(logging.DEBUG)


def mail_handler_formatter():
    return logging.Formatter(
        ' ''
            Message type:       %(levelname)s
            Location:           %(pathname)s:%(lineno)d
            Module:             %(module)s
            Function:           %(funcName)s
            Time:               %(asctime)s.%(msecs)d
            Message:
            %(message)s
        ' '',
        datefmt='%d/%m/%Y %H:%M:%S'
    )

'''