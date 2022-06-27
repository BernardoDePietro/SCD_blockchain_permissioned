from flask import Flask, json
from sqlalchemy.orm import query
from config_db import db
from werkzeug.security import generate_password_hash

class Personale(db.Model):
    __tablename__ = 'personale'
    id_personale = db.Column(db.Integer, primary_key=True)
    id_dipartimento = db.Column(db.Integer, db.ForeignKey('dipartimento.id_dipartimento'), unique=False, nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'), unique=False, nullable=False)
    nome = db.Column(db.String(50), unique=False, nullable=False)
    cognome = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)

    dipartimento = db.relationship("Dipartimento")
    categoria = db.relationship("Categoria")

    def __init__(self, id_dipartimento, id_categoria, nome, cognome, email, password):
        self.id_dipartimento = id_dipartimento
        self.id_categoria = id_categoria
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.password = generate_password_hash(password, "pbkdf2:sha256")