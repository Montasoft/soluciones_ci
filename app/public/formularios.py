from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import Form, IntegerField, SelectField, SubmitField, StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import InputRequired
#from wtforms.fields import html5
#from wtforms.fields.html5 import EmailField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename


class formContact(FlaskForm):
    nombre = StringField("Nombre", [validators.InputRequired(message= 'El nombre Completo de usuario es requerido'),validators.length(min=8,max=40, message='Ingrese su nombre completo')])
    correo = StringField("email", [validators.InputRequired(message= 'El correo electronico es requerido'), validators.Email(message='Ingrese un email valido')])
#    correo = html5.EmailField("email", [validators.Required(message= 'El correo electronico es requerido'), validators.Email(message='Ingrese un email valido')])
    teleono = IntegerField("teléfono", [validators.InputRequired(message= 'El número de teléfono es requerido'),validators.length(min=7,max=10, message='Ingrese su número de teléfono')])
    asunto = StringField("Asunto", [validators.InputRequired(message= 'El asunto es requerido'),validators.length(min=8,max=40, message='Ingrese el asunto para su mensaje')])
    mensaje = TextAreaField("Mensaje", [validators.InputRequired(message= 'El mensaje es requerido'),validators.length(min=8,max=250, message='Ingrese el contenido de su mensaje')])
    enviar = SubmitField("Enviar Form")