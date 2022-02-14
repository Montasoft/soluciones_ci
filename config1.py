from distutils.debug import DEBUG
from os.path import abspath, dirname, join
import secrets


class Config(object):
    print("llegando a config ")

    DEBUG = False
    TESTING = False
    SECRET_KEY =secrets.token_hex(28)

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Meneses1@localhost:5432/SCI_db'
    ZZZ = 'zAz'
    USUARIO_DB = 'postgresql'
    PASSWORD_DB = 'Meneses1'
    HOST_DB = 'localhost'
    PORT_DB = '5432'
    NOMBRE_DB = 'SCI_db'
    APP_SETTINGS_MODULE = 'config.DevelopmentConfig'

    FLASK_ENV="local"

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'papeleria5613837@gmail.com'
    MAIL_PASSWORD = 'meneses1'
    DONT_REPLY_FROM_EMAIL = '(papeleria5613837@gmail.com)'
    ADMINS = ('papeleria5613837@gmail.com', )
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # Define the application directory
    BASE_DIR = dirname(dirname(abspath(__file__)))

    # Media dir
    MEDIA_DIR = join(BASE_DIR, 'media')
    POSTS_IMAGES_DIR = join(MEDIA_DIR, 'posts')

    print("POSTS_IMAGES_DIR", POSTS_IMAGES_DIR)



    # Database configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/sci_db'
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/sci_db'
class StagingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/sci_db'
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/sci_db'



# SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'




# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''
