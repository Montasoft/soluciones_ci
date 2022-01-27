import os

from app import create_app
    
settings_module = os.getenv('APP_SETTINGS_MODULE')
SECRET_KEY = '7110c8ae51a4b5asdfasdfasdfef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
#SECRET_KEY =secrets.token_hex(28)

app = create_app(settings_module)



