import os

from app import create_app

import instance.config

settings_module = os.getenv('APP_SETTINGS_MODULE')
print ("*****   ", os.environ['APP_SETTINGS_MODULE'])

print("*****   ", settings_module)

app = create_app(settings_module)


