from . import public_bp
from flask import *
from flask import current_app
from flask_bootstrap import Bootstrap
from .formularios import formContact
from .models import Contacto
from app.common.mail import send_email
import os

@public_bp.route("/")  #establecer ruta inicial
def index():  #definir funcion
    return render_template('/index.html') #llamar al html


@public_bp.route("/public/contact", methods= ['GET', 'POST'])
def contact():
    form = formContact(request.form)
    if request.method == 'POST' and form.validate():
        nombre = (escape(form.nombre.data))  
        correo = (escape(form.correo.data))  
        telefono = (escape(form.telefono.data)) 
        asunto = (escape(form.asunto.data))  
        mensaje = (escape(form.mensaje.data)) 

        print("nombre: ", nombre)
        print("correo: ", correo)
        print("telefono: ", telefono)
        print("asunto: ", asunto)
        print("mensaje: ", mensaje)

        contacto = Contacto(nombre=nombre, correo=correo, telefono=telefono, asunto=asunto, mensaje=mensaje)
        contacto.save()
        print("registro guardado")

        # Enviamos un email sobre el contacto
        send_email(subject='nuevo contacto realizado en Solciones CI.com',
                   sender=os.environ['DONT_REPLY_FROM_EMAIL'],
                   recipients=['jorge.montagut@hotmail.es', ],
                   text_body=f'nombre {nombre}, correo {correo}, teléfono: {telefono}, asunto {asunto}, mensaje {mensaje}',
                   html_body=f'<p>Hola <strong>{nombre}</strong>,  correo {correo}, teléfono: {telefono}, asunto {asunto}, mensaje {mensaje} bienvenid@ al miniblog de Flask</p>')
        return redirect (url_for('public.index'))
    else:
        return render_template('contact.html', form=form)
    return render_template('contact.html', form=form)
