# instance/config.py
#postgresql://<nombre_usuario>:<password>@<host>:<puerto>/<nombre_basededatos>
from dotenv import load_dotenv
import os 
import pprint


os.environ['USUARIO_DB']= 'postgresql'
os.environ['PASSWORD_DB']= 'Meneses1'

os.environ['HOST_DB']= 'localhost'
os.environ['PORT_DB']= '5432'
os.environ['NOMBRE_DB']= 'SCI_db'
os.environ['APP_SETTINGS_MODULE']= 'config.local'

print("Estosy en instance.config.py")
load_dotenv()
env_var = os.environ

SQLALCHEMY_DATABASE_URI= 'mysql://root:@localhost/sci_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_USERNAME = 'papeleria5613837@gmail.com'
MAIL_PASSWORD = 'meneses1'


#pprint.pprint(dict(env_var), width = 1)
