from flask_login import current_user
from . import public_bp
from flask import *
from flask import current_app
from flask_bootstrap import Bootstrap
from .formularios import formContact
from .models import Contacto
from app.common.mail import send_email
import os
import logging

logger = logging.getLogger(__name__)

@public_bp.route("/")  #establecer ruta inicial
def index():  #definir funcion

#    print(app.config)
    current_app.logger.info('Llegando a la ruta del index /')
    logger.info('Llegando a la ruta del index ')
    
    logger.info("datos del currrrrrrent user", current_user)

    if current_user.is_authenticated:
        logger.info("usuario SI logggggggggggggeado")
        logger.info(current_user)
    else:
        logger.info("usuario no logggggggggggggeado")

    return render_template('/index.html') #llamar al html


@public_bp.route("/public/contact", methods= ['GET', 'POST'])
def contact():
    print("llegando a " , (__name__))
    form = formContact(request.form)
    if request.method == 'POST' and form.validate():
        print("validado")
        nombre = (escape(form.nombre.data))  
        correo = (escape(form.correo.data))  
        telefono = (escape(form.telefono.data)) 
        asunto = (escape(form.asunto.data))  
        mensaje = (escape(form.mensaje.data)) 

        logger.debug(f'nombre: {nombre}, correo: {correo}, telefono: {telefono}, asunto: {asunto}, mensaje: {mensaje}')

        
        contacto = Contacto(nombre=nombre, correo=correo, telefono=telefono, asunto=asunto, mensaje=mensaje)
        contacto.save()
        print("registro guardado")

        # Enviamos un email sobre el contacto
    

        html_body=(f'<p>Hola <strong>{nombre}</strong>,  correo {correo}, teléfono: {telefono}, asunto {asunto}, mensaje {mensaje} bienvenid@ al miniblog de Flask</p>')
        print (html_body, os.environ['DONT_REPLY_FROM_EMAIL'])
        

        send_email(subject='nuevo contacto realizado en Soluciones CI.com',
                sender=os.environ['DONT_REPLY_FROM_EMAIL'],
                recipients=['jorge.montagut@hotmail.es', ],
                text_body=f'nombre {nombre}, correo {correo}, teléfono: {telefono}, asunto {asunto}, mensaje {mensaje}',
                html_body=f'<p>Hola <strong>{nombre}</strong>,  correo {correo}, teléfono: {telefono}, asunto {asunto}, mensaje {mensaje} bienvenid@ al miniblog de Flask</p>')
    
        return redirect (url_for('public.index'))
        try:
            aasa= 'asss'
        except:
            logger.error('error al enviar')
        
    else:
        print("no validado")
        return render_template('contact.html', form=form)
    return render_template('contact.html', form=form)
