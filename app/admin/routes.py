from flask import render_template, redirect, url_for, request, escape
from flask_login import login_required, current_user, login_user, logout_user
from .models import Post, User
from . import admin_bp
from .formularios import PostForm, SignupForm, LoginForm
from werkzeug.urls import url_parse
from app import login_manager


@admin_bp.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = escape(form.title.data)
        content = escape(form.content.data)
        post = Post(user_id=current_user.id, title=title, content=content)
        post.save()
        return redirect(url_for('public.index'))
    return render_template("admin/post_form.html", form=form)


  
@admin_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        name = escape(form.name.data)
        email = escape(form.email.data)
        password = escape(form.password.data)
        # Comprobamos que no hay ya un usuario con ese email
        user = User.get_by_email(email)
        if user is not None:
            error = f'El email {email} ya está siendo utilizado por otro usuario'
        else:
            # Creamos el usuario y lo guardamos
            user = User(name=name, email=email)
            user.set_password(password)
            user.save()
            # Dejamos al usuario logueado
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.index')
            return redirect(next_page)
    return render_template("loginCrea.html", form=form, error=error)


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        
        return redirect(url_for('public.index'))
    form = LoginForm()
    if form.validate_on_submit():
        nick = (escape(form.nickname.data))
        user = User.get_by_nickname(escape(form.nickname.data))
        if user is not None and user.check_password(escape(form.password.data)):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.index')
            return redirect(next_page)
    return render_template('/login.html', form=form)


@admin_bp.route('/loginrecover')
def loginrecover():
    return "ha pedido recuperar la ontraseña"

@admin_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))