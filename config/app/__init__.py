from flask import Flask

app = Flask(__name__)

from .public import public
app.register_blueprint(public)