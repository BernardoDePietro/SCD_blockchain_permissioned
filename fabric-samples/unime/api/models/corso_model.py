from flask import Flask, json
from config_db import db

class Corso(db.Model):
    __tablename__ = 'corso'
    id_corso = db.Column(db.Integer, primary_key=True)
    id_dipartimento = db.Column(db.Integer, db.ForeignKey('dipartimento.id_dipartimento'), unique=False, nullable=False)
    nome = db.Column(db.String(100), unique=True, nullable=False)

    dipartimento = db.relationship("Dipartimento")

    def __init__(self, nome, id_dipartimento):
        self.nome = nome
        self.id_dipartimento = id_dipartimento