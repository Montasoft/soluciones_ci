import logging
from flask import Flask, render_template
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
    app = Flask(__name__, instance_relative_config=True)
#app = Flask(__name__, instance_relative_config=True)
    #app = Flask(__name__)
    
   # sqlalchemy = SQLAlchemy()
    #sqlalchemy.init_app(app)
    # load the config file specified by the APP enviroment varibale
    print("antes de config.from_object", settings_module)
    app.config.from_object(settings_module)

    db = SQLAlchemy(app)
    #migrate = Migrate(app,db)

    db.init_app(app)
    #migrate.init_app(app,db)
    #  mail.init_app(app) # iniciamos el objeto mail.
    
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)
#    app.config.from_pyfile('config.local.py', silent=True)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    configure_logging(app)
    
   # db.init_app(app)
    
    # Registro de los Blueprints
    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)
    
    # Custom error handlers
    register_error_handlers(app)

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
    

# probar par cerrar conexion
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()
   

    return app



def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404



def configure_logging(app):
    # Elimina los manejadores por defecto de la app
    del app.logger.handlers[:]
    
    loggers = [app.logger, logging.getLogger('sqlalchemy')]
    handlers = []
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(verbose_formatter())
    
    if (app.config['APP_ENV'] == app.config['APP_ENV_LOCAL']) or (
            app.config['APP_ENV'] == app.config['APP_ENV_TESTING']) or (
            app.config['APP_ENV'] == app.config['APP_ENV_DEVELOPMENT']):
        # DEBUG, INFO, WARNING , ERROR, EXCEPTION
        console_handler.setLevel(logging.DEBUG)
        handlers.append(console_handler)
    elif app.config['APP_ENV'] == app.config['APP_ENV_PRODUCTION']:
        console_handler.setLevel(logging.INFO)
        handlers.append(console_handler)
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



def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )

def mail_handler_formatter():
    return logging.Formatter(
        '''
            Message type:       %(levelname)s
            Location:           %(pathname)s:%(lineno)d
            Module:             %(module)s
            Function:           %(funcName)s
            Time:               %(asctime)s.%(msecs)d

            Message:

            %(message)s
        ''',
        datefmt='%d/%m/%Y %H:%M:%S'
    )

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

