from . import public_bp
from flask import *
from flask_bootstrap import Bootstrap
from .formularios import formContact


@public_bp.route("/")  #establecer ruta inicial
def index():  #definir funcion
    return render_template('/index.html') #llamar al html


@public_bp.route("/public/contact", methods= ['GET', 'POST'])
def contact():
    form = formContact(request.form)
    if request.method == 'POST' and form.validate():
        nombre = (escape(form.nombre.data))  
        correo = (escape(form.correo.data))  
        teleono = (escape(form.teleono.data)) 
        asunto = (escape(form.asunto.data))  
        mensaje = (escape(form.mensaje.data)) 

        print("nombre: ", nombre)
        print("correo: ", correo)
        print("teleono: ", teleono)
        print("asunto: ", asunto)
        print("mensaje: ", mensaje)

    else:
        return render_template('contact.html', form=form)
    return render_template('contact.html', form=form)
