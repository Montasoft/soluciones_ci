
import os
from os.path import abspath, dirname, join
import secrets

print("llegando a default")
os.environ['ZZZ']= 'ZETAS'
# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

# Media dir
MEDIA_DIR = join(BASE_DIR, 'media')
POSTS_IMAGES_DIR = join(MEDIA_DIR, 'posts')

# SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
SECRET_KEY =secrets.token_hex(28)

# Database configuration
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Meneses1@localhost:5432/SCI_db'
HOST_DB = 'localhost'
PORT_DB = '5432'
NOMBRE_DB = 'SCI_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

# Configuración del email
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
os.environ['DONT_REPLY_FROM_EMAIL']= 'papeleria5613837@gmail.com'
ADMINS = ('papeleria5613837@gmail.com', )
MAIL_USE_TLS = False
MAIL_USE_SSL = True


print (os.environ.get('ZZZ'))
print (os.environ.get('DONT_REPLY_FROM_EMAIL'))

print("SALIENDO de default")