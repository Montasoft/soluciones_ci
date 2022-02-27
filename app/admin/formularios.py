from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.fields import *
from flask_wtf.file import FileField, FileAllowed


class SignupForm(FlaskForm):
    nickname = StringField('NickName', validators=[DataRequired(), Length(min=5, max=20)])
    name = StringField('Nombre', validators=[DataRequired(), Length(max=80)])
    clave1 = PasswordField('Password', validators=[DataRequired()])
    clave2 = PasswordField('confirme el Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    registro = SubmitField('Registrar')


class userManager(FlaskForm):
    nickname = StringField('NickName', validators=[DataRequired(), Length(min=5, max=20)])
    name = StringField('Nombre', validators=[DataRequired(), Length(max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    is_admin = BooleanField('Administrador')
    is_Active = BooleanField('Activo')
    submit = SubmitField('confirmar')



class LoginForm(FlaskForm):
    usuario = StringField('Ingrese su Nickname o correo electrónico', validators=[DataRequired(), Length(max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    ingresar = SubmitField('Ingresar')

class formRecover(FlaskForm):
    correo = EmailField("email", validators=[DataRequired(), Email()])
    enviar = SubmitField("Recuperar Contraseña")


class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    content = TextAreaField('Contenido')
    post_image = FileField('Imagen de cabecera', validators=[
        FileAllowed(['jpg', 'png'], 'Solo se permiten imágenes')
    ])
    submit = SubmitField('Enviar')



class formCambioClave(FlaskForm):
    clave1 = PasswordField('Contraseña', 
                            validators=[DataRequired('La contraseña es requerida'),
                            Length(min=8,max=80, message='La clave debe tener entre 8 y 80 caracteres')])
    clave2 = PasswordField("Confirme la contraseña", 
                            validators=[DataRequired(message= 'La confirmacion de contraseña es requerida'),
                            Length(min=8,max=38, message='La clave debe tener entre 8 y 80 caracteres'), 
                            EqualTo('clave1', message= 'Las contraseñas deben ser iguales')])
    Cambiar_clave = SubmitField("Cambiar Contraseña")
