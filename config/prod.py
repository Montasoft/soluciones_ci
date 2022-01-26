from .default import *
import secrets

#SECRET_KEY = '5e04a4955d8asdf23e86fe6a0dfb24edb226c87d6c7787f35ba4698afc86e95cae409aebd47f7'
SECRET_KEY =secrets.token_hex(28)

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@host:port/db_name'