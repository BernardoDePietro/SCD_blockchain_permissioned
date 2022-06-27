from flask import Flask, json
from config_db import db

class Citta(db.Model):
    __tablename__ = 'citta'
    id_citta = db.Column(db.Integer, primary_key=True)
    id_nazione = db.Column(db.Integer, db.ForeignKey('nazione.id_nazione'), unique=False, nullable=False)
    nome = db.Column(db.String(50), unique=True, nullable=False)

    nazione = db.relationship('Nazione')

    def __init__(self, id_nazione, nome):
        self.id_nazione = id_nazione
        self.nome = nome

