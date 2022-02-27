from .default import *


APP_ENV = APP_ENV_DEVELOPMENT

print("estoy en config.dev.py")
#SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
SECRET_KEY =secrets.token_hex(28)

SQLALCHEMY_DATABASE_URI= 'mysql://root:@localhost/sci_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEL_LOCAL= 'DEL dev'