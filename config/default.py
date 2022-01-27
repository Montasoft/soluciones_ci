from os.path import abspath, dirname
import secrets
import app

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

SECRET_KEY = '7110c8ae51a4b5asdfasdfasdfef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
#SECRET_KEY =secrets.token_hex(28)
app.config['SECRET_KEY'] = SECRET_KEY

print(SECRET_KEY)


# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''