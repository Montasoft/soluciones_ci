import os
import config

from app import create_app

APP_SETTINGS_MODULE = config.local

settings_module = os.getenv('APP_SETTINGS_MODULE')

app = create_app(settings_module)


