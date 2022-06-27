from flask import Flask, json
from sqlalchemy.orm import query
from config_db import db
from werkzeug.security import generate_password_hash

class Promotore(db.Model):
    __tablename__ = 'promotore'
    id_promotore = db.Column(db.Integer, primary_key=True)
    id_ente = db.Column(db.Integer, db.ForeignKey('ente.id_ente'), unique=False, nullable=False) #relazione
    nome = db.Column(db.String(50), unique=False, nullable=False)
    cognome = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)

    ente = db.relationship("Ente")

    def __init__(self, id_ente, nome, cognome, email, password):
        self.id_ente = id_ente
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.password = generate_password_hash(password, "pbkdf2:sha256")