from flask import Flask, json
from sqlalchemy.orm import query
from config_db import db
from werkzeug.security import generate_password_hash

class Studente(db.Model):
    __tablename__ = 'studente'
    id_studente = db.Column(db.Integer, primary_key=True)
    id_corso = db.Column(db.Integer, db.ForeignKey('corso.id_corso'), unique=False, nullable=False) #relazione
    nome = db.Column(db.String(50), unique=False, nullable=False)
    cognome = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    matricola = db.Column(db.Integer, unique=True, nullable=False)

    corso = db.relationship("Corso")

    def __init__(self, id_corso, nome, cognome, email, password, matricola):
        self.id_corso = id_corso
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.password = generate_password_hash(password, "pbkdf2:sha256")
        self.matricola = matricola