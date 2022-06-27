from flask import Flask, json
from sqlalchemy.orm import backref, query
from config_db import db

class Universita(db.Model):
    __tablename__ = 'universita'
    id_universita = db.Column(db.Integer, primary_key=True)
    id_citta = db.Column(db.Integer, db.ForeignKey('citta.id_citta'), unique=False, nullable=False)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    via = db.Column(db.String(50), unique=False, nullable=False)
    civico = db.Column(db.String(5), unique=False, nullable=False)
    cap = db.Column(db.Integer, unique=False, nullable=False)


    citta = db.relationship('Citta')

    def __init__(self, id_citta, nome, via, civico, cap):
        self.nome = nome
        self.id_citta = id_citta
        self.via = via
        self.civico = civico
        self.cap = cap