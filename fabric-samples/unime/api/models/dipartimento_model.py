from enum import unique
from flask import Flask, json
from sqlalchemy.orm import backref, query
from config_db import db

class Dipartimento(db.Model):
    __tablename__ = 'dipartimento'
    id_dipartimento = db.Column(db.Integer, primary_key=True)
    id_universita = db.Column(db.Integer, db.ForeignKey('universita.id_universita'), unique=False, nullable=False)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    via = db.Column(db.String(50), unique=False, nullable=False)
    civico = db.Column(db.String(5), unique=False, nullable=False)
    cap = db.Column(db.Integer, unique=False, nullable=False)


    universita = db.relationship('Universita')

    def __init__(self, id_universita, nome, via, civico, cap):
        self.nome = nome
        self.id_universita = id_universita
        self.via = via
        self.civico = civico
        self.cap = cap