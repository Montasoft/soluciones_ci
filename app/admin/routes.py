import json
import random
from flask import flash, jsonify, render_template, redirect, session, url_for, request, escape, current_app
from flask_login import login_required, current_user, login_user, logout_user
from .models import Post, User, Link
from . import admin_bp
from .formularios import PostForm, SignupForm, LoginForm, formRecover, formCambioClave, PostForm
from werkzeug.urls import url_parse
from app import login_manager
from app.common.mail import send_email
import os
from werkzeug.utils import secure_filename

import logging

logger = logging.getLogger(__name__)


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        logger.info("usuario SIIIII logggggggggggggeado")
        return redirect(url_for('public.index'))
    form = LoginForm()
    if form.validate_on_submit():
        print("validate_on_submit")
        try:
            user = User.get_by_nickname(escape(form.usuario.data))
            print ("user por nickname",  user)
            if user is None: # si no existe el nickname intenta por correo
                user = User.get_by_email(escape(form.usuario.data))
                print ("user por mail",  user)
            if user is not None and user.check_password(escape(form.password.data)): 
                print("usuario logueado correctamente")
                flash ("usuario logueado correctamente", "success")
                
                login_user(user, remember=form.remember_me.data)
                session["usuario"]=user.nickname
                #session["rol"]=user[3]

                print("session:::", session)

                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('public.index')
                return redirect(next_page)

        except Exception as e:
            print(e.code)
            if e.code == 'e3q8':
                print("Error al conectarse")
                flash ("Error al conectarse a la base de datos", "danger")
            print("error", str(e))
           # return render_template('/login.html', form=form)
            #return render_template("/500.html", error = str(e))
        #finally:
    return render_template('/login.html', form=form)

  
@admin_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        nickname = escape(form.nickname.data)
        name = escape(form.name.data)
        email = escape(form.email.data)
        password = escape(form.clave1.data)

        # Comprobamos que no hay ya un usuario con ese email
        user = User.get_by_email(email)
        if user is not None:
            error = f'El email {email} ya está siendo utilizado por otro usuario'
        else:
            user = User.get_by_nickname(nickname)
            if user is not None:
                error = f'El nickname {nickname} ya está siendo utilizado por otro usuario'
            else:
                # Creamos el usuario y lo guardamos
                user = User(name=name, email=email, nickname=nickname)
                user.set_password(password)
                user.save()
                # Dejamos al usuario logueado
                login_user(user, remember=True)
                next_page = request.args.get('next', None)
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('public.index')
                return redirect(next_page)
    return render_template("loginCrea.html", form=form, error=error)



@admin_bp.route('/loginrecover', methods=['GET', 'POST'])
def loginrecover():
    form = formRecover()
    error = None
    if form.validate_on_submit():
        user = User.get_by_email(escape(form.correo.data))
        print("UUSSeer" , user)
        print(user.is_active)
        if user is not None and user.is_active:
            # genero el link para recuperar la contraseña.
            number = hex(random.getrandbits(512))[2:]
            ruta= url_for('admin.modifiClave',_external=True)+'?auth='+number

            link = Link(number=number, nickname=user.nickname, correo=user.email, estado=0)
            link.save()

            send_email(subject='nuevo contacto realizado en Solciones CI.com',
                   sender=os.environ['DONT_REPLY_FROM_EMAIL'],
                   recipients=['jorge.montagut@hotmail.es', ],
                   text_body=f'Recuperar la contraseña',
                   html_body=f'<p>{ruta} </p>')
            return render_template("loginRecov.html", form=form, error=error)

    return render_template("loginRecov.html", form=form, error=error)


@admin_bp.route("/modifiClave", methods=['GET', 'POST'])
def modifiClave():
    form = formCambioClave(request.form)
    #tomo el número enviado en el link
    tok = request.args.get('auth')
    error= None
    print ("tok: ", tok)
    # Recopero de la base de datos a partir del numero de token
    link = Link.get_by_num(tok)
    
    if link is None:
            return "Código de activación inválido"
    else:
        user = User.get_by_email(link.correo)      
    
        if request.method == 'POST' and form.validate():
            # formulario validado
            print("validado")
            clave1 = escape(form.clave1.data)
            clave2 = escape(form.clave2.data)
                #consulto las tablas de usuarios y link 

            if clave1 == clave2:
                user.set_password(clave1)
                user.save()

                return ("Contraseña cambiada")
    return render_template("modifiClave.html", form=form, error=error)


'''
                if database.modifyKey(tok,hashclave, user):
                    database.close()
                    # cerrada la conexion
                    variable = redirect(url_for('users.login'))
                    flash ("Contraseña cambiada correctamente", "success")
                    return redirect(url_for('users.login'))
            else:
                flash ("las contraseñas no coinciden", "danger")
                return redirect(url_for('users.modifiClave'))
        else:
            return render_template('modifiClave.html', form=form, usuarioActual= user) 
    else:
        flash ("Error al conectar a la base de datos", "danger")
        return redirect(url_for('users.modifiClave'))

'''

@admin_bp.route('/logout')
def logout():
    logout_user()
    session.pop("usuario",None)
    return redirect(url_for('public.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))


@admin_bp.route('/usermanager', methods=['GET', 'POST'])
def usermanager():
    #if not current_user.is_admin:
    if 1>2:
        logger.info("NO ESSSSSSSSSS ADMIN")
        return redirect(url_for('public.index'))
    else:
        users = User.get_all()
        User.shutdown_session()
        
        return render_template('/userManager.html', users= users)



@admin_bp.route('/ajaxUserManager', methods=['GET', 'POST'])
def ajaxUserManager():
    if current_user.is_admin:
        users = User.get_all()
        userArray = []
        for user in users:
            userObj = {}
            print(user.nickname)
            print( user.nickname)
            print( user.name)
            print( user.email)

            userObj['nickname'] = user.nickname
            userObj['nombre'] = user.name
            userObj['e-mail'] = user.email
            userArray.append(userObj)
        return jsonify(userArray)

#    return jsonify({'municipios' : cityArray})




     #   return jsonify(users)
        #return json.dumps(users)
















@admin_bp.route("/news", methods=["GET", "POST"])
def news():
    if not current_user.is_authenticated:
        print("usuario no  autenticado:::", current_user.is_authenticated)
        return redirect(url_for('public.index'))
    form = PostForm()
    error = None
    
    if form.validate_on_submit():
        print("Validate")
        title = escape(form.title.data)
        content = escape(form.content.data)
        file= form.post_image.data
        image_name = None
        print(file)
        # comprueba si la petición contiene la parte del fichero
        if file:
        # Si el usuario no selecciona un fichero, el navegador
        # enviará una parte vacía sin nombre de fichero
        
            image_name = secure_filename(file.filename)
            images_dir = current_app.config['POSTS_IMAGES_DIR']
            print(images_dir, "///", image_name)
            os.makedirs(images_dir, exist_ok=True)
            file_path = os.path.join(images_dir, image_name)
            file.save(file_path)  

        # Creamos el new post y guardarlo.
        
        post = Post(user_id=current_user.id, title=title, content=content)
        post.save()
        return ("post guardado correctamente")
    return render_template("newpost.html", form=form, error=error)


@admin_bp.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
#@login_required
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        print("Validate")
        title = escape(form.title.data)
        content = escape(form.content.data)
        file= form.post_image.data
        image_name = None
        print(file)
        # comprueba si la petición contiene la parte del fichero
        if file:
        # Si el usuario no selecciona un fichero, el navegador
        # enviará una parte vacía sin nombre de fichero
        
            image_name = secure_filename(file.filename)
            images_dir = current_app.config['POSTS_IMAGES_DIR']
            print(images_dir, "///", image_name)
            os.makedirs(images_dir, exist_ok=True)
            file_path = os.path.join(images_dir, image_name)
            file.save(file_path)  

        post = Post(user_id=current_user.id, title=title, content=content)
        post.archivo  = image_name
        post.save()
        return redirect(url_for('public.index'))
    return render_template("admin/newpost.html", form=form)


