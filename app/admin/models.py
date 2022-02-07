import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import synonym, sessionmaker

from app import db

class User(db.Model, UserMixin):

    __tablename__ = 'sci_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active= db.Column(db.Boolean, default=False)
    fechaCre4 = db.Column(db.DateTime(TIMESTAMP))
    nickname = db.Column(db.String(20), nullable=False)
    

    def __init__(self, name, email, nickname):
        self.name = name
        self.email = email
        self.nickname = nickname

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_nickname(nickname):
        return User.query.filter_by(nickname=nickname).first()

Session = sessionmaker()
session = Session

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('sci_user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    title_slug = db.Column(db.String(256), unique=True, nullable=False)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    archivo = db.Column(db.String(256))
    '''
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan',
                               order_by='asc(Comment.created)')

    class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='SET NULL'))
    user_name = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    '''


    def __repr__(self):
        return f'<Post {self.title}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.title_slug:
            self.title_slug = slugify(self.title)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
                self.title_slug = f'{self.title_slug}-{count}'

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def public_url(self):
        return url_for('public.show_post', slug=self.title_slug)

    @staticmethod
    def get_by_slug(slug):
        return Post.query.filter_by(title_slug=slug).first()

    @staticmethod
    def get_by_id(id):
        return Post.query.get(id)

    @staticmethod
    def get_all():
        return Post.query.all()



class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(256), nullable=False)
    estado = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Link {self.number}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        try:
            db.session.commit()
            saved = True
        except IntegrityError:
            saved = False
    
    @staticmethod
    def get_by_num(number):
        return Link.query.filter_by(number=number).first()
