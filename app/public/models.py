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

class Contacto(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    correo = db.Column(db.String(256), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
    asunto = db.Column(db.String(256), nullable=False)
    mensaje = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, nombre, correo, telefono, asunto, mensaje):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.asunto = asunto
        self.mensaje = mensaje
        

    def __repr__(self):
        return f'<Conctacto {self.nombre}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        
        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
        
    @staticmethod
    def get_all():
        return Contacto.query.all()


    def delete(id):
        contacto=Contacto.query.get(id)
        db.session.delete(contacto)
        db.session.commit()

